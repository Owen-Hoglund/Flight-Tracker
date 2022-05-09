import re

# pattern for valid email
em_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# test cases
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

valid_stayRange1 = (1, 2)
valid_stayRange2 = (5, 10)
valid_stayRange3 = (29, 30)
invalid_stayRange1 = (0, 10)
invalid_stayRange2 = (12, 9)
invalid_stayRange3 = (20, 0)
# list of tuples
testcase_stayRanges = [valid_stayRange1, valid_stayRange2, valid_stayRange3, invalid_stayRange1, invalid_stayRange2, invalid_stayRange3]

def em_isvalid(email):

    if(re.fullmatch(em_regex, email)):
        return True
    else:
        return False


def stayRange_isvalid(stayRange):

    # stayRange is a tuple
    if (stayRange[0] > stayRange [1]):
        print("Second value must be greater than first value")
        return False
    elif ((stayRange[0] or stayRange[1]) <= 0):
        print("Values must be greater than 0")
        return False
    else:
        return True

if __name__ == '__main__':

    i = 0
    length = len(testcase_emails)
    while i < length:

        if (em_isvalid(testcase_emails[i])) is True:
            print("Valid email: " + testcase_emails[i])

        elif (em_isvalid(testcase_emails[i])) is False:
            print("Invalid email: " + testcase_emails[i])
        i += 1

    i = 0
    length = len(testcase_stayRanges)
    while i < length:
        if (stayRange_isvalid(testcase_stayRanges[i])) is False:
            print('Invalid stayRange: {0}'.format(testcase_stayRanges[i]))
        elif (stayRange_isvalid(testcase_stayRanges[i])) is True:
            print('Valid stayRange: {0}'.format(testcase_stayRanges[i]))
        i += 1