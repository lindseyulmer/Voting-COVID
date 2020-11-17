# Covid and Elections
 The corona virus pandemic has created unprecedented circumstances in the United States, affecting every aspect of American life including the election process. Rising cases and concern over the government’s response to the pandemic could have greatly influenced how and who Americans voted for.
Data on corona virus cases, election results, and proportion of mail in votes are all readily available, but corona virus and election data are not readily available in the same place for comparison.
Our goal is to visualize COVID-19 and election data in the same place so that people can more easily draw conclusions about how the pandemic affected American’s political views.
# Tasks
- Gather COVID case data, 2020 election results and proportion mail in voting, 2016 election results, and poll results on COVID as a top voting issue.
- Investigate necessary packages to visualize data in interactive maps.
- Create visualizations comparing COVID cases to 2020 results for all states.
- Create visulizations comparing 2016 election results to 2020 overall and early voting results for all States.
- Create visulizations comparing COVID cases, number of mail in votes, and poll results on COVID as a top voting issue for key swing states.
# Use Cases
## Use Case 1 Interactive Map for visulazing COVID and Election Data across all states
- Read in Covid and Election data as data frames and merge to one data frame
- Use Geopandas package to add state shapes to data frame
- Use Bokeh to perform plotting/visualization (also to save plot to file)
- Use Bokeh to make the plot interactive to better illustrate the data
## Use Case 2 Interactive Map for visulazing Election Data from the 2020 and 2016 election across all states
- Read in 2016 and 2020 election results and 2020 early voting turnout for all states as separate dataframes then merge to one
- Use Geopandas package to add state shapes to data frame
- Use Bokeh to perform plotting/visualization (also to save plot to file)
- Use Bokeh to make the plot interactive to better illustrate the data
## Use Case 3 Interactive Map for visualizing COVID cases, mail in voting data, and poll data for key swing states
- Alter COVID case data dataframe to include only key swing states
- Read in mail in voting data and poll data as separate dataframes and merge to one with the covid data
- Use Geopandas package to add state shapes to data frame
- Use Bokeh to perform plotting/visualization (also to save plot to file)
- Use Bokeh to make the plot interactive to better illustrate the data
