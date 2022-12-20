from behave import *
from MainApp.StartApp import main
use_step_matcher("parse")


@given("that the manager forgot to attach a file")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.arguments = ["script_name"]


@when("the application starts")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.r_value = main(context.arguments)


@then('the error message: "Employee file missing" will be shown')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.r_value == "Employee file missing"


@given("that the manager attached a file that doesn't have the employees data")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.arguments = ["script_name", ".\\miscellaneous_file.txt"]


@then('the error message: "Unrecognized format" will be shown')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.r_value == "Unrecognized format"


@given("that the manager attached a file")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.arguments = ["script_name", ".\\test_employee_data.txt"]


@then("a dictionary with the names and schedules worked each day will be computed for all employees")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expected_result = {
        "RENE": [(10.25, 12.0), (10.0, 12.0), (None, None), (13.0, 13.25), (None, None), (14.0, 18.0), (20.0, 21.0)],
        "ASTRID": [(10.0, 12.0), (None, None), (None, None), (12.0, 14.0), (None, None), (None, None), (20.0, 21.0)]
    }
    assert context.r_value == expected_result
