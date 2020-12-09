# Covid and Elections

## Software Components
The software components are importing data, structuring data to one dataframe and adding shapefile information for use with Geopandas, and creating and exporting the interactive map with Bokeh. Summarizing it is importing data, reformatting data, and creating and exporting map visualizations.

## Possible Components
### `make_plot`: make plots with the preloaded data
- input: dataset with multiple variables
- output: plots including bar charts, scatter plots, etc.
### `add_data`: prepare data to create figure
- input: Two data sets as csvs, the new one that's being added on and a datafile containing geopandas shape information
- output: one combined data set as a csv
### `interaction`: increase user interaction in plots
- input: figures
- output: figures

## Interactions To Accomplish Use Cases
The imported data with be combined by the reformatting component to one data frame, and that data frame will be used
by the visualization creation component. General steps for this are:
- Reading in data (import component)
- Merging data to one data frame (reformat component)
- Using the Geopandas package to add state shapes to a data frame (reformat component)
- Using Bokeh to perform plotting/visualization (also to save the plot to file) (visualization component)
- Using Bokeh to make the interactive plot to better illustrate the data (visualization component)

## Preliminary Plan
- Gather COVID case data, 2020 election results and proportion mail-in voting, 2016 election results, and poll results
- Investigate necessary packages to visualize data in interactive maps.
- Create visualizations comparing COVID cases to 2020 results for all states.
- Create visualizations comparing 2016 election results to 2020 overall and early voting results for all States.
- Create visualizations comparing COVID cases, number of mail-in votes, and poll results on COVID as a top voting issue for key swing states.
