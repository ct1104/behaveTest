class SendMobile(object):

    def __init__(self, person=None,type=None):
        self.type = type
        self.person = person

    def decision(self):
        assert self.person is not None
        if "mom" in self.person:
            return "mom"
        elif "dad" in self.person:
            return "dad"
        else:
            return "none"




from behave   import given, when, then
from hamcrest import assert_that, equal_to, is_not

@given(u'i have an {type} mobile')
def step_impl1(context,type):
    context.sendmobile = SendMobile(type)
    context.sendmobile.type = type
    print ("mobile is:"+type)

@when(u'the mobile is {type}')
def step_impl2(context,type):
    if type == "red" :
        context.sendmobile.person ="mon"
    else:
        context.sendmobile.person ="dad"
    print ("send to "+context.sendmobile.person)

@then(u'i send it to {who}')
def step_impl3(context,who):
     print ("i send it to "+who)
     assert_that(who, equal_to(context.sendmobile.decision()))

 