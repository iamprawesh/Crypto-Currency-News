from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeText

register = template.Library()
# # form .models

@register.filter(name='cut')
def cut(value,args):
    return (value[0:10])