### IAM_tools
The IAM_tools is command line utility to query data from [AMPERE Scenario database](http://www.iiasa.ac.at/web/home/research/researchPrograms/Energy/AMPERE_Scenario_database.html).
Input data are comma separated value [csv] file.

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
If teh output arg is omitted the result will be printed to console.

##### Examples

Run help:
```python
filter_AIM -h
```
Print all unique models:

```python
filter_IAM iam_input.csv -unique model
```
     
Print all rows where models are GCAM or REMIND to console output:
```python
filter_AIM iam_input.csv -model 'GCAM|REMIND'
```
   
Print unique regions of rows where model is GCAM:
```python
filter_AIM iam_input.csv -model GCAM -unique region
```
     
Export all rows where variable column start with Emissions|CO2 to my_output.csv file:
```python
filter_AIM iam_input.csv -variable 'Emissions\|CO2*' -output my_output.csv
```

