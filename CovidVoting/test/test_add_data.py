"""This module has tests for add_data.py
class TestAddData(unittest.TestCase)
test_oneshot(self)
test_smoke(self)
test_edge(self)
"""
import unittest
import sys
import pandas as pd
from CovidVoting.add_data import (add_data_csv,
                                  add_data_shapefile)
sys.path.append('..')

# Define all states
all_states = ["Maryland", "Iowa", "Delaware", "Ohio",
             "Pennsylvania", "Nebraska", "Washington",
             "Alabama", "Arkansas", "New Mexico", "Texas",
             "California", "Kentucky", "Georgia", "Wisconsin",
             "Oregon", "Missouri", "Virginia", "Tennessee",
             "Louisiana", "New York", "Michigan", "Idaho",
             "Florida", "Illinois", "Montana", "Minnesota",
             "Indiana", "Massachusetts", "Kansas", "Nevada", "Vermont",
             "Connecticut", "New Jersey", "District of Columbia",
             "North Carolina", "Utah", "North Dakota", "South Carolina",
             "Mississippi", "Colorado", "South Dakota", "Oklahoma", "Wyoming",
             "West Virginia", "Maine", "New Hampshire", "Arizona",
             "Rhode Island"]
# Define key states
key = ["Arizona", "Florida", "Georgia", "Michigan",
       "Minnesota", "North Carolina", "Ohio",
       "Pennsylvania", "Texas", "Wisconsin"]
# prepare data for one shot test
covid = pd.read_csv("data/raw_2_covid_latest.csv")
election = pd.read_csv("data/use_election.csv")
election = election.loc[election['state'].isin(all_states)]
merge_covid_election = pd.merge(left=covid, right=election, how='right',
                             left_on='State/Territory', right_on='state')

class TestAddData(unittest.TestCase):
    """
    This class defines the tests for add_data_shapefile
    and add_data_csv
    """
    def test_smoke(self):
        """Smoke Tests
        Args:
            self
        Returns:
            True: Test passed
            False: Test failed
        """
        add_data_shapefile('data/coviddataand2020Election.csv',
                           'data/raw_7_keystates_covid_voting_issue_poll.csv',
                           'NAME', 'States', key,
                           "CovidVoting/test/keystates_covid_2020voting_poll.csv")

    def test_smoke_add_data_csv(self):
        """smoke test"""
        base_data = "./data/raw_2_covid_latest.csv"
        new_data = "./data/use_election.csv"
        base_state_col = 'State/Territory'
        new_state_col = 'state'
        use_state = all_states
        how_join = 'right'
        df_covid_election = add_data_csv(base_data, new_data, base_state_col,
                                       new_state_col, use_state, how_join)
        self.assertIsNotNone(df_covid_election)

    def test_oneshot(self):
        """One shot tests
        Args:
            self
        Returns:
            True: Test passed
            False: Test failed
        """
        df = pd.read_csv(
          "CovidVoting/test/keystates_covid_2020voting_poll.csv",
          index_col=0)
        df2 = pd.read_csv('data/keystates_covid_2020voting_poll.csv',
                          index_col=0)
        self.assertEqual(
                         df.columns.all(), df2.columns.all())

    def test_oneshot_add_data_csv(self):
        """oneshot test"""
        base_data = "./data/raw_2_covid_latest.csv"
        new_data = "./data/use_election.csv"
        base_state_col = 'State/Territory'
        new_state_col = 'state'
        use_state = all_states
        how_join = 'right'
        df_covid_election = add_data_csv(base_data, new_data, base_state_col,
                                       new_state_col, use_state, how_join)
        pd.testing.assert_frame_equal(df_covid_election, merge_covid_election)

    def test_edge(self):
        """Edge Tests
        Args:
            self
        Returns:
            True: Test passed
            False: Test failed
        """
        with self.assertRaises(KeyError):
            add_data_shapefile('data/basedata.csv',
                               'data/raw_3_2020election.csv',
                               "wrongname", "States", all_states,
                               "testresults.csv")

    def test_edge(self):
        """Edge Tests
        Args:
            self
        Returns:
            True: Test passed
            False: Test failed
        """
        with self.assertRaises(KeyError):
            add_data_csv('data/basedata.csv',
                         'data/raw_3_2020election.csv',
                         "wrongname", "States", all_states,
                         "testresults.csv")

if __name__ == '__main__':
    unittest.main()
