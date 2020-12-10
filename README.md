# Voting-COVID
[![Build Status](https://travis-ci.org/lindseyulmer/Voting-COVID.svg?branch=main)](https://travis-ci.org/lindseyulmer/Voting-COVID)
The purpose of this project is to visualize COVID and election data on the same plot, so that people can better discern the political ramifications of the pandemic.
## Directory Structure
- CovidVoting: This directory holds the code for preparing data for visualization and making interactive plots to show Covid counts and voting results simultaneously. It also contains unit tests to prove the functionalities of each module.
- data: This directory contains data downloaded from multiple sources, including election results data from 2016 and 2020, Covid related data, and shapefile data that stores the geometric information of the United States.
- docs: This directory contains documentation including the functional specification, the design specification, the component specification and the final project presentation.
- example: This directory includes examples of using the functions in the CovidVoting directory.

Voting-COVID/
  |- README.md
  |- CovidVoting/
     |- __init__.py/
     |- main.py/
     |- add_data.py/
     |- make_plot_2020_and_2016.py/
     |- make_plot_swingstate.py/
     |- tests/
        |- __init__.py/
        |- test_add_data.py/
        |- test_make_plot_2020_and_2016.py/
        |- test_make_plot_swingstate.py/
  |- example/
     |- demo_swingstate.gif/
     |- plot_swingstate.html/
  |- data/
     |- __init__.py/
     |- shapefiles/
        |- __init__.py/
        |- cb_2018_us_state_20m.shp/
     |- raw_1_covid_daily.csv/
     |- raw_2_covid_latest.csv/
     |- raw_3_2020election.csv/
     |- raw_5_2016election.csv/
     |- raw_6_2016mail.csv/
     |- use_election.csv/
     |- raw_7_keystates_covid_voting_issue_poll.csv/
     |- raw_8_2020_votebymail.csv/
  |- docs/
     |- Component_Specification.md/
     |- Design.md/
     |- Functional_Specification.md/
     |- TechnologyReview.pdf/
     |- __init__.py/
  |- __init__.py/
  |- environment.yml/
  |- .travis.yml/
  |- LICENSE/
  |- .coveragerc/
  |- .gitignore/
  


## Tutorial for adding data and creating a plot (the most complicated use case)
### Step 1: Download Data
Clone the github repo so that you have all necessary functions.
Prepare the data you will be adding as a csv.
### Step 2: Add Data
Use the add_data function from add_data.py to add your desired data. It is recommended to use basedata.csv from the data directory as the starting directory so that you
are adding your data onto to a csv that already contains the necessary geopandas information. The basedata.csv contains geopandas and cdc covid case data.

![](example/demo_swingstate.gif)
