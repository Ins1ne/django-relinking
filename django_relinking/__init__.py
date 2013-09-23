# coding: utf-8
from django.conf import settings
from django_relinking.models import Link


link_template = getattr(
    settings, "RELINKING_LINK_TEMPLATE",
    '<a target="{target}" href="{url}">{text}</a>'
)
index_pattern = '<%=link {}=%>'


def relink_text(origin):
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
    return origin
