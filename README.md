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
basis. The simple example would be that if a company has a need for its employees or clients to travel for which: 
1. They expect to reimburse many employees for travel cost
2. The exact date of travel is inconsequential in the long term

Then they can use their database of employees, and their corresponding home airports, to determine the most cost effective date for that
conference within a certain range (a given quarter or month, for example).

## Notes

- This project uses MySQL workbench to store all of the required databases. To use the software you will need to fill out your own information 
in the dataBaseManager to work on your machine. 
- As of right now, I havent found a suitable API to populate the flight prices with real current data. For a number of reasons, I am choosing to
forgo this for the time being: Firstly, I do not want to pay for an API for this project as it could become costly. Secondly, as a proof of concept,
I implemented random data generation capability which is sufficient to prove the software works given real data. However, should I ever want to connect 
an API, I believe it would take minimal effort to implement and no revision to the code, only the addition of a few new functions (API calls, a minimal
data processing). 

## File Guide
- Setup.py contains functions to initialize the database required for the program to run
- groupFlights.py contains the current user interface which for now is only a command line interface
- dataBaseManager contains all the code to interact with the database using SqLite. It pushes group information in, updates prices for flights,
populates the various tables in the database, etc,.
- flightGroupService.py contains some test cases for email validation etc,. Currently not implemented in the main code.
- exampleGroupGenerator.py contains a function to generate random flight groups for testing purposes
- flightGroupClassMk2.py contains the core class we use to hold all information related to a given group
- groupHandlerClass.py is a class which can hold instances of groups for use in the data base manager
- flightProjectHelper contains various utility functions which are used repeatedly throughout the program (date time conversion etc,).
