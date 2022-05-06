# Flight-Tracker
## Track flights for friends or enterprise

This project is designed to track flights for groups of people coming from multiple locations to one destination together.


## Personal Use

Say you have two friends from Boston, three from Minneapolis, one from Toronto, and two from LA,
and you are all interested in travelling to Madrid. This application would then track when the price for the entire group, on average,
is at its lowest. Ideally once you find this price, everyone splits the cost of all the tickets evenly so that everyone benefits from the 
aggregate price being low.

## Enterprise Use
The basic idea can be extended quite easily for use on a large scale for businesses which fly employees or clients on a regular (and planned)
basis. The simple example would be that if a company has a conference for which: 
1. They expect to reimburse many employees for travel cost
2. The exact date of the conference is inconsequential

Then they can use their database of employees, and their corresponding home airports, to determine the most cost effective date for that
conference within a certain range (a given quarter or month, for example).

## Development Instructions
Run `MinorTestEnvironmentMk2.py`:

output: 
```
Group Information: 
---------------------------------------------------------------------
Your group is interested in traveling to: BOS
Sometime between 2022-12-16 and 2023-01-22
And you are interested in a stay of 5 to 17 days
Your contact email address is: ZdGe@gmail.com
---------------------------------------------------------------------
Traveler origins:
9  Travelers from SYD
3  Travelers from HRM
4  Travelers from AHE
6  Travelers from YYZ
9  Travelers from PVG
```