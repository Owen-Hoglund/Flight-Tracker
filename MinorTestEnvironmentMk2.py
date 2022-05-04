from cgi import test
from groupHandlerClass import handler
import flightGroupClassMk2
import TestHandler
import exampleGroupGenerator

testGroup = exampleGroupGenerator.random_group_maker()
testGroup.printinfo()
print (type(testGroup))