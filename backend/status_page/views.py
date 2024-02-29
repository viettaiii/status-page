from django.shortcuts import get_object_or_404, render


# ...
def index(request):
    return render(request, "index.html")


def history(request):
    return render(request, "history.html")


def detail(request):
    return render(request, "detail.html")
