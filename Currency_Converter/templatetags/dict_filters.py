from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
@register.filter
def rounding(obj,num):
    return round(float(obj.fAmount),3)
@register.filter
def flag(dictionary,value):
    for i in dictionary:
        if dictionary[i]== value:
            break
    return i
