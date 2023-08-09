# DSSE-SRE-Assignment

Problem Statement - 
The Accounting team would like to quickly look up country codes to speed up
processing of expense reports, they currently have a website bookmarked and the
process is manual and tedious. Help them speed things up by creating a simple cli.
 Write a country lookup service using your favorite programming language.
 Explore the following API https://www.travel-advisory.info/api
 Given country code -&gt; return country name example:
lookup --countryCode=AU
Australia

 Save the data from https://www.travel-advisory.info/api to a file called
data.json and add functionality to your program to work with a file instead of
real api endpoint
 Make sure your program supports multiple country codes as input
 Be ready to demo execution of your program in the terminal


Solution - 

Created a python code for county lookup service - lookup_requests.py
Terminal commands to get the desired output are present in - terminal commands

This program is like a digital assistant for the Accounting team. They want to quickly find country names based on country codes instead of using a manual website. The program does this for them.

It talks to an online service (API) that has a list of countries and their codes.
The team can tell the program a country code, and it will tell them the country name. For example, if they say "AU," it will reply "Australia."
The program can save the list of countries and codes to a file, so the team doesn't have to go online every time. It's like saving notes on your computer.
The program also knows how to read the saved list from the file.
