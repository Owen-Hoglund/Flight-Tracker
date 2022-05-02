from groupHandlerClass import handler
import flightGroupClassMk2
import TestHandler
# Checks to see that the code is able to create an instance of the class, pickle it, unpickle it into a new instance
# While mainting equivalence in attributes. Passing this method 1 does this from a premade instance, passing 2
# will prompt the user to instantiate the instance with their own input
# TestHandler.origin_list_test_protocol(1)
TestHandler.origin_list_test_protocol(2)


control = handler()
control.load()
control.printall(control)