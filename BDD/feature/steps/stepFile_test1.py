from behave import *
from tests.test_file1 import Test1


@given(u'Home Page Display')
def step_impl(context):
    Test1.test_check_title(context)


@given(u'Check Menu List is present')
def step_impl(context):
    Test1.test_side_nav_present(context)


@given(u'Practice Board is present')
def step_impl(context):
    Test1.test_board_present(context)


@then(u'Check all the demo listed down in Basic section')
def step_impl(context):
    Test1.test_all_demo_btn_present(context)
    # raise NotImplementedError(u'STEP: Then Check all the demo listed down in Basic section')


@When(u'Validate if get input form is working')
def step_impl(context):
    Test1.test_get_input(context)


@then(u'Validate if get input total form is working')
def step_impl(context):
    Test1.test_get_input_total(context)

