# Module 3 Challenge: Analysis of the Election Audit

## Overview of Election Audit
Seth and Tom are analyzing election results. Election commision has asked to answer the following:
* The voter turn out for each county
* The percentage of votes from each county out of the total count
* The county with the largest number of votes

### Purpose
Goal of this project is to refractor our previuos python code and use it to extract the requested information above.
## Election-Audit Results
* **How many votes were cast in this congressional election?**
Total number of votes was 369,711.
* **Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.**
All the votes were casted in 3 counties:
Jefferson :  10.5% (38855 votes)
Denver :  82.8% (306055 votes)
Arapahoe :  6.7% (24801 votes)
* **Which county had the largest number of votes?**
Denver county had the largest turnout.
* **Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.**
There were three candidates:
Charles Casper Stockham: 23.0% (85,213 votes)
Diana DeGette: 73.8% (272,892 votes)
Raymon Anthony Doane: 3.1% (11,606 votes)
* **Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**
Winner was Diana DeGette with 272,892 votes which was 73.8% of the total votes

## Election-Audit Summary
This code can be used to analyze any election results. There are few limitations in the implementation. 

1- If the number of votes is the same for two (or more) candidates, the script only pick one of them as the winner. 

2-The same is true for the county turn out. if the counties have the same number of voters, only one of them is picked as the winner. 

These limitations can be addressed so that this code can be used to analyze any election result.
Also, the way that the input data is passed on to the script can be upgraded. Instead of using a CSV file, it can get its data from the cloud or a voting machine, etc.
