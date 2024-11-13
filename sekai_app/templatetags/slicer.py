from django import template

register = template.Library()

@register.filter
def slice_list(value, arg):
    arg = int(arg)
    return [value[i:i + arg] for i in range(0, len(value), arg)]