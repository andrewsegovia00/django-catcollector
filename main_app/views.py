from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat


# Create your views here.


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def cats_index(request):
    cats = Cat.objects.all()
    return render(
        request,
        "cats/index.html",
        {
            "cats": cats,
        },
    )


# second parameter is the same name as the variable name in the route which was cat_id
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(
        request,
        "cats/detail.html",
        {
            "cat": cat,
        },
    )


class CatCreate(CreateView):
    model = Cat
    fields = "__all__"


class CatUpdate(UpdateView):
    model = Cat
    fields = ["breed", "description", "age"]


class CatDelete(DeleteView):
    model = Cat
    success_url = "/cats/"
