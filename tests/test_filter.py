import os
import sys
import pandas as pd

TESTPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(TESTPATH, '..'))

from iam_tools.filter import filter  # NOQA

df = pd.read_csv(os.path.join(TESTPATH, 'iam_test.csv'), delimiter=',')


def test_model_filter():
    """Test retrieving unique model names"""

    res = filter(df, **{'model': "GCAM"})
    assert len(res.model.unique()) == 1
    assert res.model.unique()[0] == "GCAM"

    res = filter(df, **{'model': "GCAM|REMIND"})
    assert len(res.model.unique()) == 2
    assert res.model.unique()[0] == "GCAM"
    assert res.model.unique()[1] == "REMIND"


def test_scenario_filter():
    """Test retrieving unique model names"""

    res = filter(df, **{'scenario': "AMPERE2-450-NucOff-HST"})
    assert len(res.scenario.unique()) == 1
    assert res.scenario.unique()[0] == "AMPERE2-450-NucOff-HST"

    res = filter(df, **{'scenario': "^AMPERE2.*"})
    scenario_list = res.scenario.unique()
    for scenario in scenario_list:
        assert scenario.startswith("AMPERE2")

    res = filter(df, **{'scenario': "450-.*.-OPT"})
    scenario_list = res.scenario.unique()
    for scenario in scenario_list:
        assert "450-" in scenario
        assert "-OPT" in scenario


def test_variable_filter():
    res = filter(df, **{'variable': "^Secondary Energy\|Electricity\|.*"})
    res_list = res.variable.unique()
    for item in res_list:
        assert item.startswith("Secondary Energy|Electricity|")
