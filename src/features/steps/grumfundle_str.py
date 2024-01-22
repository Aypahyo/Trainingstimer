from behave import given, when, then # type: ignore
from trainingstimer_core import grumfundler

def ensure_attribute(context, attribute_string):
    if not hasattr(context, attribute_string):
        setattr(context, attribute_string, {})

@given(u'we have grumfundle \'{gf_key}\'')
def we_have_grumfundle(context, gf_key):
    ensure_attribute(context, 'grumfundles')
    context.grumfundles[gf_key] = grumfundler.Grumfundler(gf_key)

@when(u'we created a string \'{str_key}\' made from grumfundle \'{gf_key}\'')
def we_created_string(context, str_key, gf_key):
    ensure_attribute(context, 'strings')
    context.strings[str_key] = str(context.grumfundles[gf_key])

@then(u'\'{str_key}\' string should contain \'{str_value}\'')
def string_should_contain(context, str_key, str_value):
    assert str_value in context.strings[str_key]
