"""This module has tests for add_data.py
class Testadd_data(unittest.TestCase)
test_oneshot(self)
test_smoke(self)
test_edge(self)
"""
import unittest
from CovidElection import add_data
#Define all states
allstates=["Maryland", "Iowa", "Delaware", "Ohio", "Pennsylvania", "Nebraska", "Washington",
        "Alabama", "Arkansas", "New Mexico", "Texas", "California", "Kentucky", "Georgia",
        "Wisconsin", "Oregon", "Missouri", "Virginia", "Tennessee", "Louisiana", "New York",
        "Michigan", "Idaho", "Florida", "Illinois", "Montana", "Minnesota", "Indiana",
        "Massachusetts","Kansas","Nevada","Vermont", "Connecticut","New Jersey",
        "District of Columbia","North Carolina","Utah","North Dakota",
         "South Carolina","Mississippi","Colorado","South Dakota","Oklahoma","Wyoming",
        "West Virginia", "Maine","New Hampshire","Arizona","Rhode Island"]
#Define key states
key=["Arizona", "Florida", "Georgia", "Michigan", "Minnesota", "North Carolina", "Ohio",
         "Pennsylvania", "Texas", "Wisconsin"]
class TestAddData(unittest.TestCase):
    def test_smoke(self):
        """Smoke Tests
        Args:
            self
        Returns:
            True: Test passed
            False: Test failed
        """
        add_data.add_data('data/basedata.csv','data/raw_3_2020election.csv',"NAME","States",
        allstates, "data/coviddataand2020Election.csv")
    def test_oneshot(self):
        """One shot tests
    Args:
        self
    Returns:
        True: Test passed
        False: Test failed
    """
        self.assertEqual(add_data.add_data('data/coviddataand2020Election.csv',
        'data/raw_7_keystates_covid_voting_issue_poll.csv',
        'NAME','States', key, "keystates_covid_2020voting_poll.csv"),"data/keystates_covid_2020voting_poll.csv" )
    def test_edge(self):
        """Edge Tests
        Args:
            self
        Returns:
            True: Test passed
            False: Test failed
        """
        with self.assertRaises(TypeError):
            add_data.add_data('data/basedata.csv','data/raw_3_2020election.csv',"wrongname",
            "States", allstates, "testresults.csv")
unittest.main()
