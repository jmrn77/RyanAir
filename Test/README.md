RYAN AIR TEST
=============

* TEST EXECUTION

- Install required packages executing (from "Test"):
    pip install -r requirements.txt

- From "Test", execute:
    behave features/payment --junit


* NOTES
- I prefer to implement the test case using Python 2.7 instead of Java because it is more flexible and faster.
- Install packages
- I could implement the test by classic PageObject definition but I prefer to move the logic to steps and
  keep in the PageObjects the web element definitions.
- Prerequisites:
  Testing user created: josemiguel.rodrigueznaranjo@gmail.com
- "_output/screenshots" folder is created to save screenshots of each failed test execution.
- I like to ease the configuration, so data related to each environment are stored in a Yaml file (in my opinion,
  the easiest way to manage data in a file) and loaded in a dictionary structure before beginning the execution.
- Same for dependent texts of language. Each language texts are stored in a Yaml file in loadde in a dictionary.
- Reporting is generated to be loaded with Junit.
- In each scenario definition, I like to tag a lot. It is useful to
- I have fixed package versions in requirements.txt because I like to assure the compatibility.
- I organize features by functionality ("payment") enabling customize environments.
- Created "common" directory to group common steps used in different feature folders.
- In booking process I select “One Way” because the target of the test case is to check a declined payment and
  selecting it, the test is easier and quicker.
- "From" and "Destination" cities are selected to assure more than one daily flight.
- ChromeDriver is included.
