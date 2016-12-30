from behave import step

@step('{word:w} step passes')
def step_passes(context, word):
    pass

@step('{word:w} step fails')
def step_fails(context, word):
    assert False, "XFAIL-STEP"
