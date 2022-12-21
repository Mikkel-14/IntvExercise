# ioet's programming exercise

## Problem description

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame.

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2

Example 2:

INPUT:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 3

The solution shouldn’t need any UI, a console application is good enough.

## Approach and methodology

This application is being developed using a behaviour-driven development approach. This way, the testing is focused in
verifying the value creation stated on the requirements, using primarily natural language. A brief description of the
process done for developing this solution is stated below.

1. Requirements gathering with user stories (documented on `.feature` files)
2. Test scenarios documented using natural language (on `.feature` files)
3. Class design, test implementations in code (under the `features\steps` directory)
4. Implementation of actual functionalities
5. Test execution

## Solution's overview

> *Note: This section focuses particularly in the algorithms implemented to solve the most valuable functionality of the application*

The program takes as input a plain text file (`.txt`) and parses the information of the schedule for each employee. 
Then, the program runs two algorithms:
- The first computes all the posible pais of employees (n choose 2), taking as input the employees' names
- The second uses the pairs and checks day by day if both employees were in the office at the same time frame. This is done by verifying whether the time intervals contained one in the other, or if one interval overlapped with the other one.

Finally, the program prints the results, if any, or prints that no coincidence was found.

This application uses an object-oriented architecture, which allowed the implementation of the Strategy Pattern, used for File handling classes.
The complete class blueprint used for the application is shown in [the app design file](AppDesign.puml).

## Instructions for running the program locally

### Requisites
- Python 3.10
- Behave library (can be installed using `pip install behave`)
- A Windows machine (the program was only tested for Windows)

### Usage
- For test execution, run the command `behave` inside the `IntvExercise` folder
- For executing the actual program, run `python main.py FILENAME` inside the `IntvExercise` folder. `FILENAME` should be replaced with a path to a text file. **For example**, to try the program we could run `python main.py .\test_employee_data.txt`

> **Important** 
> Since the application was developed and tested on Windows, it's recommended to have all the project files in CRLF format.
> Particularly, for the feature files.

