# 0x00 AirBnB Clone- The Console

- Introduction
This is a team project, the first step to building a clone of the AirBnB; the Console.

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

The console will perform the following tasks:

* Create a new object
* Retrive an object from a file
* Do operations on objects
* Destroy an object


- Installation
git clone https://github.com/PreshusMcCoy/AirBnB_clone.git
change to the AirBnb directory and run the command:

 ./console.py


- Execution
In interactive mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$


In Non-interactive mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$


- Testing
All the test are defined in the tests folder.

Documentation
Modules:
python3 -c 'print(__import__("my_module").__doc__)'
Classes:
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
Functions (inside and outside a class):
python3 -c 'print(__import__("my_module").my_function.__doc__)'


and


python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'


- Python Unit Tests
* Unittest module
* File extension .py
* Files and folders star with test_
* Organization:for models/base.py, unit tests in: tests/test_models/test_base.py
* Execution command: python3 -m unittest discover tests
or: python3 -m unittest tests/test_models/test_base.py


Run test in interactive mode
echo "python3 -m unittest discover tests" | bash

Run test in non-interactive mode
To run the tests in non-interactive mode, and discover all the test, you can use the command:

python3 -m unittest discover tests


- Usage
* Start the console in interactive mode:
$ ./console.py
(hbnb)

* Use help to see the available commands:
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)

* Quit the console:
(hbnb) quit
$
