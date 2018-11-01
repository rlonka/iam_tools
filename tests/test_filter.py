import os
import sys
import pytest
import pandas as pd
from pandas.util.testing import assert_frame_equal

TESTPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(TESTPATH, '..'))

from iam_tools.filter import filter

df = pd.read_csv('iam_test.csv', delimiter=',')

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
        assert scenario.startswith("AMPERE2") == True
