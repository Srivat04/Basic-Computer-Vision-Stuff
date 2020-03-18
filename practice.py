/***********************************************************************************************************************************************/

#os is module which has functions to interact with the operating system
#Some important functions in the os module are as follows

os.getcwd()  #Gets the current working directory in python

also import sys

sys.path.append("<Directory name>")   #includes this directory in the environment path,now we can load modules from this path




/***********************************************************************************************************************************************/

#Python code for string formatting

data = ("John","Doe",53.3)
print("Hello %s %s, your current balance is %f" % data)

/*************************************************************************************************************************************************/

#Basic String operations

string = "Hello World"
len(string)        #Prints the length of the string
string.index("o")  #Prints the index of the first occurence in that string

# and some other basic stuff...............

/*************************************************************************************************************************************************/

#Use of 'in' and 'is' operators

selected_list = ["John","Thot","Varun"]
name = "Varun"
if name in selected_list :
	print("Congo!!!You are selected")
else :
	print("Better luck next time")

/*************************************/
\*  #Important catch                 *\
/*  x = [1,2,3]                      */
\*  y = [1,2,3]                      *\
/*  print(x == y) # Prints out True  */      
\*  print(x is y) # Prints out False *\  
/*************************************/   #Basically it means the x is not same as y.

/*******Meaning, take a look at this code*************************/
x = [1,2,3,4]
y = x
x is y // (or y is x anyway it means the same) 
#The output is true!!!


list.index(element)   #gives the index of the element in the list



/*************************************************************************************************************************************************/

#Loops in python!!!!!!!

#forloop

for variable in list 			#Basically prints the list
	print(variable)

#whileloop

while condition
	operation

#To search for strings with specific substrings in python we can use this following code

matching_strings = [string for string in list if "substring" in string]

#To sort a list in alphabetical order we can use the following command or code or whatever

list.sort()

/***************************************************************************************************************************************************/

#Functions in Python!!!

def list_benefits():
	return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(string):
	return string + " is a benefit of functions !"

list = list_benefits()
for string in list:
	sentence = build_sentence(string)
	print(sentence)


/****************************************************************************************************************************************************/

#Class in Python !!!

class MyClass:
    variable = "blah"
    def function(self):
        print("At last,you've managed to access the function inside the class!!!")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)
myobjectx.function()

#Exercise

class Vehicle:
	name = ""
	kind = "car"
	color = ""
	value = 100.00
	def description(self):
	    desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
	    return desc_str


car1 = Vehicle()
car1.name = "Fer"
car1.kind = "Convertible"
car1.color = "Red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "Van"
car2.color = "Blue"
car2.value = 10000.00

car1.description()
car2.description()

/***********************************************************************************************************************************************/

#Modules in Python
#Modules are just the python code stored as <module name>.py and can be accessed using the import command
#To import functions we can use this command from <module_name> import <fn_name>
#To use functions we can use <module_name>.<fn_name>
#To import all the functions and objects we can use from <module_name> import* command
#To import a module as another name,use import <module_name> as <name>
dir(<module_name>)  #returns a list of all attributes

Also learn how to write packages





/***********************************************************************************************************************************************/

#Using Numpy,we should convert normal array to numpy array in order to perform efficient computations.

import numpy as np
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_weight_kg = np.array(weight_kg)

weight_lbs = np_weight_kg*2.2


