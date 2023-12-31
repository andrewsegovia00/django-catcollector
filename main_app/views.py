from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat
from .forms import FeedingForm


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
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(
        request,
        "cats/detail.html",
        {
            # include the cat and feeding_form in the context
            "cat": cat,
            "feeding_form": feeding_form,
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


# add this new function below cats_detail
def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect("detail", cat_id=cat_id)
