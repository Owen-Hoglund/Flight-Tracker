import re
import datetime
from datetime import date

# pattern for valid email
em_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# email test cases
valid_em1 = 'sample@email.com'
valid_em2 = 'madeup.dude7@test.com'
valid_em3 = 'tester7@internet.com'
invalid_em1 = 'badboy.com'
invalid_em2 = 'wrong.format@'
invalid_em3 = 'bad@website'
invalid_em4 = '@email.net'
invalid_em5 = '@email'
invalid_em6 = 'alsobad@.net'
# list of strings
testcase_emails = [valid_em1, valid_em2, valid_em3, invalid_em1, invalid_em2,
                  invalid_em3, invalid_em4, invalid_em5, invalid_em6]

def em_isValid(email):

    if(re.fullmatch(em_regex, email)):
        return True
    else:
        return False

# stayRange test cases
valid_stayRange1 = (1, 2)
valid_stayRange2 = (5, 10)
valid_stayRange3 = (29, 30)
invalid_stayRange1 = (0, 10)
invalid_stayRange2 = (12, 9)
invalid_stayRange3 = (20, 0)
# list of tuples
testcase_stayRanges = [valid_stayRange1, valid_stayRange2, valid_stayRange3, invalid_stayRange1, invalid_stayRange2, invalid_stayRange3]

def stayRange_isValid(stayRange):

    # stayRange is a tuple
    if (stayRange[0] > stayRange [1]):
        print("Second value must be greater than first value")
        return False

    elif ((stayRange[0] or stayRange[1]) <= 0):
        print("Values must be greater than 0")
        return False

    else:
        return True

# date test cases (note: validity dependent on TODAY's date)
valid_dateRange1 = ('2023-01-09', '2023-01-22')
valid_dateRange2 = ('2022-06-10', '2023-01-22')
valid_dateRange3 = ('2022-08-23', '2022-09-08')
valid_dateRange4 = ('2023-04-01', '2023-04-29')
invalid_dateRange1 = ('2023-12-01', '2023-12-22')
invalid_dateRange2 = ('2022-06-14', '2023-06-13')
invalid_dateRange3 = ('2022-07-23', '2022-07-23')

# combining upper/lower into one function 
# datetime should give us methods to validate this rather than RegEx-ing
def dateLowerUpper_areValid(dateLowerBound, dateUpperBound):
    pass

if __name__ == '__main__':

    i = 0
    length = len(testcase_emails)

    while i < length:

        if (em_isValid(testcase_emails[i])) is True:
            print("Valid email: " + testcase_emails[i])

        elif (em_isValid(testcase_emails[i])) is False:
            print("Invalid email: " + testcase_emails[i])
        i += 1

    i = 0
    length = len(testcase_stayRanges)

    while i < length:
        if (stayRange_isValid(testcase_stayRanges[i])) is False:
            print('Invalid stayRange: {0}'.format(testcase_stayRanges[i]))

        elif (stayRange_isValid(testcase_stayRanges[i])) is True:
            print('Valid stayRange: {0}'.format(testcase_stayRanges[i]))

        i += 1

    today = date.today()
    print(today)
    print('Today: ' + str(today))
    print(today.weekday())
    tdelta = datetime.timedelta(days=7)
    print(today-tdelta) # gives us the date from a week ago
    fourthOfJuly = datetime.date(2022, 7, 4) # no leading zeroes here
    print('Fourth of July:  {}'.format(fourthOfJuly))

# - dateLowerBound
    # - The beginning of the range of dates the group is interested in travelling
    # - [ ] Must be a string in the format YYYY-MM-DD
    # - [ ] Must be at least one day in the future (current date + one day)
    # - [ ] Must be within a year of the current date
    # - [ ] MM must be a valid entry
    #     - [ ] Not greater than 12
    #     - [ ] Not less than 1
    #     - [ ] Months 1-9 must be formatted with a prefixed zero (sept = 09, sept != 9)
    # - [ ] DD Must be a valid entry
    #     - [ ] Not greater than the number of days in the associated month
    #     - [ ] Not less than zero
    #     - [ ] Same prefix zero rule as months (01, 02, etc,.)

# - dateUpperBound
#     - The end of the range of dates the group is interested in travelling
#     - [ ] Must be a string in the format YYYY-MM-DD
#     - [ ] Must be at least dateLowerBound + the upper bound of the stayRange
#     - [ ] MM must be a valid entry
#         - [ ] Not greater than 12
#         - [ ] Not less than 1
#         - [ ] Months 1-9 must be formatted with a prefixed zero (sept = 09, sept != 9)
#     - [ ] DD Must be a valid entry
#         - [ ] Not greater than the number of days in the associated month
#         - [ ] Not less than zero
#         - [ ] Same prefix zero rule as months (01, 02, etc,.)