from email import generator
from msilib.schema import File
import mysqlx

from pure_eval import group_expressions
import groupHandlerClass
import flightGroupClassMk2
import exampleGroupGenerator
import dataBaseManager



# This code will
# 1. Create ten random flight groups using the generator
# 2. FORMAT the pickle file and then pickle those ten group_expressions
# 3. Table the pickled groups 
# 4. FORMAT the pickle File
# 5. Restore the pickle file using the table of groups in mysql


handler = groupHandlerClass.handler()
for i in range(10):
    newGroup = flightGroupClassMk2.flightGroup
    newGroup = exampleGroupGenerator.random_group_maker()
    handler.newGroup(newGroup)
handler.save()
dataBaseManager.groupTabler(handler)

del handler
handler = groupHandlerClass.handler()
handler.load()
