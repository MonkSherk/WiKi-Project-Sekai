from django import template
import re

register = template.Library()

@register.filter
def youtube_id(value):
    regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(regex, value)
    if match:
        return match.group(1)
    return ''
