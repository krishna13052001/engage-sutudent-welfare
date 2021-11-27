from django import template
register = template.Library()

import datetime

@register.simple_tag
def returnDays(value):
    difference = value - datetime.date.today()
    return difference.days

register.filter('returnDays', returnDays)