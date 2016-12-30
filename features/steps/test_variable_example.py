class ContactExample(object):
    
    TRANSFORMATION_MAP ={
        "13755199114":"1234",
        "15801204212":"1289",
        }

    def __init__(self,mobile= None,code = None):
        self.mobile = mobile
        self.code = code
        
    
    @classmethod   
    def getMap(clf,mobile):
        return clf.TRANSFORMATION_MAP.get(mobile,"DIRT")
        

    def decision(self):
        assert self.mobile is not None
        assert self.code is not None
        



from hamcrest import assert_that, equal_to, is_not
from behave import *

    
@given('i have an valid "{mobile}"')
def step_impl_smobile(context,mobile):
    context.contact = ContactExample()
    context.contact.mobile = mobile
    
@when('input the mobile')
def step_impl_imobile(context):
    pass
    
@then('get the "{code}"')
def step_impl_getcode(context,code):
    context.contact.code = context.contact.getMap(context.contact.mobile)
    assert_that(code,context.contact.code)
    
 
