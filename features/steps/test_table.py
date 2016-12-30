class Contact(object):
    
    TRANSFORMATION_MAP ={
        "13755199114":"1234",
        "15801204212":"1289",
        }

    def __init__(self):
        self.mobile = []
        self.code = []
        
    def add(self,mobile,code):
        self.mobile.append(mobile)
        self.code.append(code)
    
    @classmethod   
    def getMap(clf,mobile):
        return clf.TRANSFORMATION_MAP.get(mobile,"DIRT")
        

    def decision(self):
        assert self.mobile is not None
        assert self.code is not None
        




from behave   import given, when, then
from hamcrest import assert_that, equal_to, is_not

@given(u'i have an valid mobile and a right code')
def step_impl1(context):
    context.contact = Contact()
    for row in context.table:
        print row["mobile"],row["code"]
        context.contact.add(row["mobile"],row["code"])

@when(u'input mobile "{mobile}"')
def step_impl2(context,mobile):
    context.currentmobile = mobile
@then(u'get the code "{code}"')
def step_impl3(context,code):
    context.currentcode = context.contact.getMap(context.currentmobile)
    print ("mobile:"+context.currentmobile)
    print ("code:"+context.currentcode)
    assert_that(code, equal_to(context.currentcode))

 