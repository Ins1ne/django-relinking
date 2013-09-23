# coding: utf-8
from django import template
from django.conf import settings
from django.core.cache import cache
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
        link_template = '<a target="{target}" href="{url}">{text}</a>'
        index_pattern = '<%=link {}=%>'
        links = []
        for link in Link.objects.all():
            for key in link.keys_list:
                i = len(links)
                links.append(link_template.format(
                    target=dict(Link.TARGET_CHOICES)[link.target],
                    url=link.url,
                    text=key
                ))
                origin = origin.replace(key, index_pattern.format(i))
        for i, link in enumerate(links):
            origin = origin.replace(index_pattern.format(i), link)
        relinked = origin
        cache.set(key, relinked)
    return relinked
