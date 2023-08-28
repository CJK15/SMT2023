# SMT2023
2023 SMT Challenge Submission
List of Python Scripts and Their Purposes: 
Scripts were developed in Google Colab

Backup Data Preparation:
This script includes the interface for users to determine whether or not a backup play occurred. To use this script, users need input game data to run this script. Data extracted accounts for variables throughout the play. 

Backup Statistical Analysis:
This script takes each csv created in the Backup Data Preparation script, combines the information for fly-ball outcomes during backup plays. The script then compares each variable by using the net-deviation from the median. 

Functions no plots:
This script is required for the Initial analysis mentioned in the paper. This is the same exact code as the Backup Data Preparation script; however, the plots and backup situation prompts are turned off since the initial analysis would like to look at every fly-ball situation in the outfield at the moment the ball was caught. 

Code to Run Data Prep (all plays):
This code simply runs the Functions no plots script which makes the interface easier for the user to use and export data. The Functions no plots script is required to run this script as well as all game data. 

Initial Statistical Analysis:
This script takes the data exported in the Code to Run Data Prep script (which exports data by team), combines the four team csv files and conducts T-Tests on the data. 

List of CSV Files and Their Purposes:
CSVfileCaught.csv and CSVfileDropped.csv are the csv files which are the concated files of all dropped and caught fly-ball plays in which a backup situation occurred. This file was created in the Backup Statistical Analysis script. 

TeamA1, TeamA2,TeamA3, TeamB1 csv files are all fly-ball out caught and dropped variables for all plays. These files are created using the Code to Run Data and analyzed in the Initial Statistical Analysis script. 

