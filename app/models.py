# coding: utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django_relinking.content_types import register


class SomeModel(models.Model):

    status = models.IntegerField(choices=[(0, "unpublished"), (1, "published")], default=0, null=False)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('display_model', args=[self.pk])

    class Meta(object):
        verbose_name = "example model"
        verbose_name_plural = "example models"


register(SomeModel, objects=lambda: SomeModel.objects.filter(status=1))
