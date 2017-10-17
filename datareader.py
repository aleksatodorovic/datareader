"""
Alex Todorovic
Tulane University
Machine Learning
Project Data Reader


This is a data reader that uses the built in python library csv to read in selected features from ten seasons of
premier league games. The program iterates through each csv file picking out seven values per row.
It appends these values as a list to the list of samples, appropriately named 'samples'.


Note: If you are checking whether or not this works do not write 'print(samples)' at the end of the program this
made IDLE unresponsive for me. Instead, try iterating through samples and printing each element. Also, this will take a
bit of time to finish as each season has 380 games which makes for 3800 games in total.
"""


import csv

#list of csv files used in for loop
season_list = ['07-08.csv','08-09.csv','09-10.csv','10-11.csv','11-12.csv','12-13.csv','13-14.csv','14-15.csv','15-16.csv','16-17.csv']

#this is the 2D array where I'll be storing my samples
samples = []
for season in season_list:
    with open(season, newline='') as csvfile:
        league = csv.reader(csvfile, delimiter='?', quotechar='|')
        for row in league:
            #prepping data into a list
            row = ','.join(row)
            row = row.split(',')
            #features: home team, away team, home goals, away goals, result, home shots, away shots
            samples += [row[2],row[3],row[4],row[5],row[6],row[11],row[12]]
        

