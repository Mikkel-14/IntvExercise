from behave import *
from FileManager.File import PlainTextFile
from FileManager.Parser import PlainTextParser
from MainApp.EmployeeRoster import EmployeeRoster
from MainApp.PairGenerator import EmployeePairGenerator
from MainApp.OutPutter import StringOutPutter
use_step_matcher("re")


@given("the employee report")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    with open('test_file_2.txt', 'wb') as f:
        f.write(bytes(context.text, "UTF-8"))

    context.employee_info = PlainTextFile('test_file_2.txt', PlainTextParser()).parse()


@when("the employee coincidence is computed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.coincidences = EmployeeRoster(context.employee_info).compute_coincident_employees(EmployeePairGenerator())


@then('the application should return the message: "No coincident employees were found!"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expected = "No coincident employees were found!"
    actual = StringOutPutter().format(context.coincidences)
    assert expected == actual


@then("the application must return the following coincidences")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    actual = StringOutPutter().format(context.coincidences)
    assert context.text.strip('\r') == actual
