from django.shortcuts import render


def index(request):
    """
    A view to return the index page
    NB brands and categories given in contexts.py
    """

    return render(request, 'home/index.html')
