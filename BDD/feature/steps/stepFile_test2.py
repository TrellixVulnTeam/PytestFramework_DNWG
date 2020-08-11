from behave import *
from tests.test_file2 import Test2


@given(u'User is on Check demo page and verify check box is display and working')
def step_impl(context):
    Test2.test_single_check_box(context)


@Then(u'Verify multiple check box')
def step_impl(context):
    Test2.test_multiple_check_box(context)

