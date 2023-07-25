from django.shortcuts import render

# Create your views here.

# Usually a Model is used
cats = [
    {"name": "Lolo", "breed": "tabby", "description": "furry little demon", "age": 3},
    {"name": "Sachi", "breed": "calico", "description": "gentle and loving", "age": 2},
]


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def cats_index(request):
    return render(
        request,
        "cats/index.html",
        {
            "cats": cats,
        },
    )
