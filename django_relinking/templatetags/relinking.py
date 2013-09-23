# coding: utf-8
from django import template
from django.conf import settings
from django.core.cache import cache
from django_relinking import relink_text
from django_relinking.models import Link

from hashlib import md5


register = template.Library()
prefix = getattr(settings, "RELINKING_CACHE_PREFIX", Link._meta.db_table)


@register.filter
def relink(origin):
    """
    Replaces original value by appling context
    """
    key = "{}.{}".format(prefix, md5(origin).hexdigest())
    relinked = cache.get(key, None)
    if relinked is None:
        relinked = relink_text(origin)
        cache.set(key, relinked)
    return relinked
