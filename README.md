### IAM_tools

The IAM_tools is command line utility to query data from
[AMPERE Scenario database](http://www.iiasa.ac.at/web/home/research/researchPrograms/Energy/AMPERE_Scenario_database.html).
Input data are comma separated value [csv] file.

For testing purpose there is small test file following IAM structure:
tests/iam_test.csv

#### Installation
IAM_tools can be installed directly from gitlab repository:

```pip install git+https://gitlab.com/dlab-indecol/iam_tools.git --upgrade```

#### Usage

The IAM_tools can be used to filter, query and export data from IAM.
The command line tool is ```filter_IAM```
The filter use [regexp](https://docs.python.org/3.6/howto/regex.html)
when selecting values from columns.
The columns to filter are: mode, region, scenario, variable.
The utility can be used to show unique values of this columns.
Selection can be exported to csv, mat and h5 output file.
If the output arg is omitted the result will be printed to console.

##### Examples

Run help:
```python
filter_IAM -h
```

###### Viewing unique entries for a specific index

Print all unique models:

```python
filter_IAM iam_input.csv -unique model
```

Print to console unique regions of rows where model is GCAM:

```python
filter_IAM iam_input.csv -model "GCAM" -unique region
```

###### Selecting rows based on the index

Print to console all rows where variables starts with "Capacity|Electricity|":
```python
filter_IAM iam_input.csv -variable "^Capacity\|Electricity\|.*"
```

Note, that the vertical bar '|' has a special meaning in regex (as the or symbol). Thus to match
the literal character '|' you have to escape it with a backslash ('\\').

Export all rows where variable column start with Secondary Energy|Electricity| 
to my_output.mat [cell array] file:
```python
filter_IAM iam_input.csv -variable "^Secondary Energy\|Electricity\|.*" -output my_output.mat
```

Export all rows where variable column start includes 450- and -OPT  to my_output.csv file:
```python
filter_IAM iam_input.csv -variable "450-.*.-OPT" -output my_output.csv
```
     
Print to console all rows where models are either GCAM or REMIND:
```python
filter_IAM iam_input.csv -model "GCAM|REMIND"
```
     
Export all rows where variable column start with Emissions|CO2 to my_output.csv file:
```python
filter_IAM iam_input.csv -variable "Emissions\|CO2*" -output my_output.csv
```

#### Contributing

If you find a bug or have suggestions for improvement please use the
[Issue Tracker](https://gitlab.com/dlab-indecol/iam_tools/issues) for communication.
Development follows a gitlab centric workflow, thus if you want to contribute fork the repository
 and file a merge request when you are finished.


#### Authors

* Radek Lonka
* Konstantin Stadler

#### License

BSD 3-Clause License

Copyright (c) 2018, [Industrial Ecology Digital Lab](https://iedl.no) at NTNU