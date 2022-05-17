import groupHandlerClass
import flightGroupClassMk2
import exampleGroupGenerator
import dataBaseManager



# This code will create ten random groups, FORMAT the pickle file, write them to the pickle file, and then table the data into the database

handler = groupHandlerClass.handler()
for i in range(10):
    newGroup = flightGroupClassMk2.flightGroup
    newGroup = exampleGroupGenerator.random_group_maker()
    handler.newGroup(newGroup)
    #newGroup.printinfo()
handler.save()
dataBaseManager.groupTabler(handler)

del handler
handler = groupHandlerClass.handler()
handler.load()
for group in handler.groups:
    print("TEST")
    group.printinfo()
