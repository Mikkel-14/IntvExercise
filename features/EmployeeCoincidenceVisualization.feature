# language: en
  Feature: Employee coincidence visualization
    As a manager, I want to visualize the pairs of employees and the number of times they have coincided
    in the office, so that I can find the root cause of the external circumstances that recently happened.

  Scenario: There weren't any coincident employees
    Given the employee report
    """
    RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
    ASTRID=MO12:00-13:00,TH14:00-15:00
    """
    When the employee coincidence is computed
    Then the application should return the message: "No coincident employees were found!"

  Scenario: There exist coincident employees
    Given the employee report
    """
    RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
    ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
    ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
    """
    When the employee coincidence is computed
    Then the application must return the following coincidences
    """
    RENE-ASTRID: 2,RENE-ANDRES: 2,ASTRID-ANDRES: 3
    """