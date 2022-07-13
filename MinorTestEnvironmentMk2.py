from email import generator
from msilib.schema import File
from tkinter import GROOVE
import mysqlx

from pure_eval import group_expressions
import groupHandlerClass
import flightGroupClassMk2
import exampleGroupGenerator
import dataBaseManager
import flightProjectHelper as utility

iata_pair = 'BOS-MSP'
iata = 'MSP'

print(utility.departure_or_return(iata, iata_pair))