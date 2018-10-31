"""
Filter the IAM csv file and export the subset.
The filter use regexp for each selector.
"""

import sys
import argparse
import pandas as pd
import scipy.io as sio

selectors = ['model', 'scenario', 'region', 'variable']
output_formats = ['mat', 'csv', 'h5']


def filter(df, **kwargs):
    """
    Filter pandas.DataFrame using keywords arguments selectors.
    The values of selectors are processed as regexp.

    Parameters
    ----------
    df: pandas DataFrame
        Input dataframe to be filtered.
    kwargs:
        Selectors to filter using regexp.
        The selectors as a kwargs keys are:
            - model
            - scenario
            - region
            - variable

    Returns
    -------
    pandas.DataFrame
        The filtered subset of original input DataFrame.

    """
    df.columns = map(str.lower, df.columns)

    for param in kwargs.items():
        df = df[df[param[0]].str.contains(param[1], regex=True)]
        df = df.reset_index(drop=True)
    return df


def export(df, output_file=None):
    """
    Export pandas DataFrame to output file with specified format.
    If the output_file is None teh DataFrame will be output
    to console std out.

    Parameters
    ----------
    df: pandas DataFrame
        Input dataframe to be filtered.
    output_file: str
        Output filename path with specified format which can be .csv, .mat or .h5.
        If None the console std out will be used.

    Raises
    ------
    NotImplementedError
        If not supported file format is used

    """
    if output_file:
        if output_file.endswith('.csv'):
            df.to_csv(output_file, index=False)
        elif output_file.endswith('.mat'):
            df = df.add_prefix('col_')
            d = df.to_dict(orient='list')
            sio.savemat(output_file, d)
        elif output_file.endswith('.h5'):
            df.to_hdf(output_file, key='test', index=False)
        else:
            raise NotImplementedError("The output format: {} is not supported."
                                      .format(output_file.split('.')[-1]))

    else:
        df.to_string(sys.stdout, index=False)


def main():
    """
    main function
    """
    parser = argparse.ArgumentParser(description="Filter csv file with IAM data.")
    parser.add_argument("input", help="path to input IAM csv file file")
    parser.add_argument("-unique", type=str,
                        help="Show unique values of specified column. The result will be"
                             "printed to standard console output.")
    parser.add_argument("-model", type=str,
                        help="Model selection")
    parser.add_argument("-scenario", type=str,
                        help="Scenario selection")
    parser.add_argument("-region", type=str,
                        help="Region selection")
    parser.add_argument("-variable", type=str,
                        help="Variable selection")
    parser.add_argument("-output", type=str,
                        help="Output file name. The filename should contain format"
                             "in of output structure. If none provided the output"
                             "will be csv file. If not supported file format is used,"
                             "the script will raise error.")
    args = parser.parse_args()
    args_dict = vars(args)

    params = {selector: args_dict[selector] for selector in selectors if args_dict[selector]}

    df = pd.read_csv(args.input, delimiter=',')

    res_df = filter(df, **params)

    # we always print to console if user wants unique values
    if args_dict['unique']:
        out = list(res_df[args_dict['unique']].unique())
        sys.stdout.write(", ".join(str(x) for x in out))
        sys.exit(0)

    export(res_df, args_dict['output'])


if __name__ == "__main__":
    main()
