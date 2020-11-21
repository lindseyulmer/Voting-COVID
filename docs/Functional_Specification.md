# Covid and Elections

## Project Scope
- Our Goal: Visualize COVID-19 and election data in the same place so that people can more easily draw conclusions about how the pandemic affected American’s political views.
- Background: The coronavirus pandemic has created unprecedented circumstances in the United States, affecting every aspect of American life including the election process. Rising cases and concern over the government’s response to the pandemic could have greatly influenced how and who Americans voted for. 
Data on coronavirus cases, election results, and the proportion of mail-in votes are all readily available, but coronavirus and election data are not readily available in the same place for comparison. 

## Data Sources
- <a href= 'https://covid.cdc.gov/covid-data-tracker/#cases_casesper100klast7days'>COVID-19 Cases Data</a>: COVID-19 Cases Data will be downloaded from the CDC's website as a CSV file.
- <a href= 'http://healthyelections.org/map/'>2016 vote by mail data</a>: 2016 vote by mail data will be downloaded from healthy elections.org as a CSV file.
- <a href= 'https://www.fec.gov/documents/1890/federalelections2016.xlsx'>2016 overall election results</a>: 2016 overall election results will be downloaded from the FEC as an excel spreadsheet. 
- <a href= 'https://www.commonwealthfund.org/publications/2020/sep/election-2020-battleground-state-health-care-poll'>Poll data on covid as a voting issue</a>: Poll data on covid as a voting issue will be downloaded from commonwealthfund.
- <a href= 'https://www.nbcnews.com/politics/2020-elections/president-results'>2020 results</a>: 2020 results will be copied from nbcnews.com as a CSV.
- <a href= 'https://www.washingtonpost.com/graphics/2020/elections/early-voting-numbers-so-far/'>2020 results</a>:  2020 early voting data will be copied from the washingtonpost into a CSV.
- <a href= 'https://www.theguardian.com/us-news/2020/nov/04/mail-in-ballot-tracker-us-election-2020'>2020 mail-in voting data</a>: 2020 mail-in voting data will be copied from the guardian into a CSV.
* Some of this data had to be copied into spreadsheets instead of downloaded as a table because the data was not available in a downloadable format at the time of this project because results were still being finalized.

## User Profile
The user can be anyone who is interested in visualizing covid and election data. This can be anyone from people who work in public policy to just citizens who are interested in the election or covid data. They do not need experience with python but should be comfortable using a Jupyter Notebook to create the figures.

## Use Cases
### Use Case 1: User Creating Figure with Data that's preuploaded
User will run existed Jupyter Notebook as is to generate the desired interactive map figure.
### Use Case 2: User Adding Additional Data to Figures
If the user had additional data they wanted in an interactive map, they could upload more data, and alter what columns in the combined data frame are plotted to include their newly added data. Users doing this should have some experience with python and Jupyter Notebook.
### Use Case 3: User Interacting with Pre-generated Figures
If a user was only interested in the data we uploaded in the view it was exported as, they could just download the figure and interact with it. This requires the least level of 
familiarity with Jupyter Notebook and python so is the most accessible.
