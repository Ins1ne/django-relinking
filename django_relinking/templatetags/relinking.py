# coding: utf-8
from django import template
from django.conf import settings
from django_relinking import relink_text
from django_relinking.models import Link


register = template.Library()


@register.filter
def relink(origin):
    """
    Relink origin text
    """
    return relink_text(origin)
