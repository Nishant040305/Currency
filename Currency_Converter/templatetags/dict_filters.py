from django import template
"""function to be used in the template"""


register = template.Library()

@register.filter
def get_item(dictionary, key):#to get value in dict using key
    return dictionary.get(key)
    
@register.filter
def rounding(obj,num):#to round of the digits in history 
    return round(float(obj.fAmount),3)
    
@register.filter
def flag(dictionary,value):# to get the key using value
    for i in dictionary:
        if dictionary[i]== value:
            break
    return i
