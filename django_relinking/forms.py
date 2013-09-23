# coding: utf-8
from django import forms
from django.core.urlresolvers import reverse
from django_relinking.content_types import content_types_choices, objects_choices
from django_relinking.models import Link


class LinkForm(forms.ModelForm):

    model = Link

    def __init__(self, *a, **k):
        super(LinkForm, self).__init__(*a, **k)
        types_choices = content_types_choices()
        self.fields["content_type"].widget = forms.Select(
            choices=types_choices,
            attrs=dict(get_objects_url=reverse("get_content_type_objects"))
        )
        ctype = (
            self.data.get("content_type")
            or self.initial.get("content_type")
            or self.instance.content_type
            or (types_choices and types_choices[0][0])
        )
        choices = objects_choices(ctype) if ctype else []
        self.fields["object_pk"].widget = forms.Select(choices=choices)

        is_object_required = -1 not in dict(choices)

        self.fields["content_type"].required = is_object_required
        self.fields["object_pk"].required = is_object_required

        self.fields["direct_link"].required = not is_object_required

    class Media(object):
        js = ("js/django-relinking.js",)
