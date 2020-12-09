# Voting-COVID
[![Build Status](https://travis-ci.org/lindseyulmer/Voting-COVID.svg?branch=main)](https://travis-ci.org/lindseyulmer/Voting-COVID)
The purpose of this project is to visualize COVID and election data on the same plot, so that people can better discern the political ramifications of the pandemic.
## Directory Structure
## Tutorial for adding data and creating a plot (the most complicated use case)
### Step 1: Download Data
Clone the github repo so that you have all necessary functions.
Prepare the data you will be adding as a csv.
### Step 2: Add Data
Use the add_data function from add_data.py to add your desired data. It is recommended to use basedata.csv from the data directory as the starting directory so that you
are adding your data onto to a csv that already contains the necessary geopandas information. The basedata.csv contains geopandas and cdc covid case data.

![](example/demo_swingstate.gif)
