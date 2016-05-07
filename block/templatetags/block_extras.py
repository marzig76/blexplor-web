from django import template
import datetime

register = template.Library()


@register.filter
def date_format(value):
    return datetime.datetime.fromtimestamp(
            value).strftime('%Y-%m-%d %H:%M:%S')


@register.filter
def satoshis2btc(value):
    return value / 100000000.0
