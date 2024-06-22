from django import template
register = template.Library()

@register.filter(name='roli')
def roli(roles, i):
    """Return the rol[i]"""
    return roles[i]