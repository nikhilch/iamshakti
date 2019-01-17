import re
from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, urlname):
    """
    This function compares the request path against the supplied urlname to
    determine which navbar link should be considered `active`. If no match is
    found, then an empty string is returned.
    """
    try:
        pattern = '^\\' + reverse(urlname)
    except NoReverseMatch:
        pattern = ''

    # A special case for when the path is `/`
    if pattern == '^\/':
        pattern = '^\/$'

    current_path = context['request'].path
    if re.search(pattern, current_path):
        return 'active'

    return ''
