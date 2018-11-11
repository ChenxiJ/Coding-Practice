Problem link: </br>
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

A simple policy for warning clients about possible fraudulent account activity. 
If the amount spent by a client on a particular day is greater than or equal to 2 times the client's median spending for 
a trailing number of days *d*, they send the client a notification about potential fraud. No notifications in the first *d* days.

Given *d* and an array of integers representing daily expenditures *expenditure* (all expenditures are between 0 and 200),
find the total number of times the client receives a notification over that period.