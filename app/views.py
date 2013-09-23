# Create your views here.
from django.shortcuts import render
from django.views.generic import View
from django_relinking.content_types import register

from app.models import SomeModel


class CustomView(View):

    def get(self, request):
        return render(request, "app/hello.html")


register(CustomView, "Custom view")


def index(request):
    return render(request, "app/index.html", dict(
        objects=SomeModel.objects.filter(status=1).all()
    ))


def show(request, pk):
    return render(request, "app/show.html", dict(
        obj=SomeModel.objects.get(pk=pk)
    ))
