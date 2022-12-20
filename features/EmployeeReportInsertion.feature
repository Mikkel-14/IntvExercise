#language: en
  Feature: Employee report insertion
    As a manager, I want to attach a text file with all employees' names and schedules worked in office during a week, so
    that I don't need to type all of them one by one in the application.

    Scenario: No file was attached
      Given that the manager forgot to attach a file
      When the application starts
      Then the error message: "Employee file missing" will be shown

    Scenario: A file with incorrect format was attached
      Given that the manager attached a file that doesn't have the employees data
      When the application starts
      Then the error message: "Unrecognized format" will be shown

    Scenario: A file was attached with correct data
      Given that the manager attached a file
      When the application starts
      Then a dictionary with the names and schedules worked each day will be computed for all employees


      
