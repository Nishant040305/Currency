from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
@register.filter
def rounding(obj,num):
    return round(float(obj.fAmount),3)
