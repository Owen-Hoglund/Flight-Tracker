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
# list
testcase_emails = [valid_em1, valid_em2, valid_em3, invalid_em1, invalid_em2,
                  invalid_em3, invalid_em4, invalid_em5, invalid_em6]

def em_isvalid(email):

    if(re.fullmatch(em_regex, email)):
        return True
    else:
        return False

if __name__ == '__main__':

    i = 0
    length = len(testcase_emails)
    while i < length:

        if (em_isvalid(testcase_emails[i])) is True:
            print("Valid email: " + testcase_emails[i])

        elif (em_isvalid(testcase_emails[i])) is False:
            print("Invalid email: " + testcase_emails[i])
        i += 1