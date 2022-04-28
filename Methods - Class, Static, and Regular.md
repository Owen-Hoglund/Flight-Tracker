---
aliases: [Static Methods, Class Methods]
---
## Class Methods
- Automatically takes the _class_ as the first argument (by convention `cls`)
- to make a method into a class method, use the [[decorator]] `@classmethod`

for example
```Python
	@classmethod 
	def set_raise_amt(cls, amount):
	cls.raise_amt = amount

#this is using our class method
Employee.set_raise_amt(1.05) # it is equivalent to:
# Employee.raise_amt = 1.05
print(Employee.raise_amount) # yields 1.05
print(emp_1.raise_amount) # yields 1.05
print(emp_2.raise_amount) # yields 1.05
``` 
NOTE: we cant use `class` instead of `cls` because `class` is reserved in python

You can run class methods from within instances as well, much as we did in the [[Class Variables]] tutorial where we set the raise amount from the instance, HOWEVER, in this case, because the method takes the _CLASS_ as the argument, it will set the amount for EVERY instance, not just the instance the method was run from. This is NOT recommended.

Class Methods as Alternative Constructors

You can use class methods as another way to construct objects. For example, if we had the situation of needing to create a new instance of employee through a string in a file or something similar, rather than parse and instantiate them as follows:
```Python
emp1_str = "john-Doe-70000"
emp2_str = "jane-Doe-60000"
emp3_str = "Jim-Ding-80000"
first, last, pay = emp1_str.split('-')
new_emp1  = Employee(first, last, pay)
```

we can create a new `classmethod` to intantiate them in this way for us.

```Python
@classmethod
def from_string(cls, emp_str)
	#The line below takes a string of employee info, parses it
	first, last, pay = emp_str.split('-')
	# The line below creates an instance of the class employee, and returns it
	return cls(first, last, pay)
```

Now, rather than manually constructing it, a user can simply call upon the much simpler _Alternative Constructor_ `from_string`
```Python
new_emp = Employee.from_string("John-Deere-70000")
# is completely identical to 
new_emp = Employee("john", "Deere", 70000)
#which they would have had to parse manually otherwise
```


## Static Methods
When working with classes, regular methods automatically pass the instance as the first argument, Class methods automatically pass the class as the first argument. Static methods dont pass _anything_ as an argument. We include them in our classes because they have some logical connection with the class

For example, say we want to take in a date, and find out whether or not that was a work day, it has a logical connection to the class but does not rely upon any instance or class variable.
```Python
	@staticmethod
	def is_work_day(day):
		if day.weekday() == 5 or f day.weekday() == 6:
			return False
		return True
```

A dead give away for whether a function should be static is if you dont require access to any attribute or method from the class or instance. As above. 

In the next Section we will begin a review of [[Inheritance]]