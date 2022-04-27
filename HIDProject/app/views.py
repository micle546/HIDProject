"""
Definition of views.
"""

from datetime import datetime
from typing_extensions import Required
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def test(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/test.html',
        {
            'title':'Test',
            'message':'test page',
            'year':datetime.now().year,
        }
    )

def reptiles(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/reptiles.html',
        {
            'title':'Reptiles',
            'message':'test page',
            'year':datetime.now().year,
        }
    )

def mammals(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/mammals.html',
        {
            'title':'Mammals',
            'message':'test page',
            'year':datetime.now().year,
        }
    )

def amphibians(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/amphibians.html',
        {
            'title':'Amphibians',
            'message':'test page',
            'year':datetime.now().year,
        }
    )

def birds(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/birds.html',
        {
            'title':'Birds',
            'message':'test page',
            'year':datetime.now().year,
        }
    )

def fish(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fish.html',
        {
            'title':'Fish',
            'message':'test page',
            'year':datetime.now().year,
        }
    )

def invertebrates(request):
    """Renders the test page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/invertebrates.html',
        {
            'title':'Invertebrates',
            'message':'test page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'HIC Group Project',
            'year':datetime.now().year,
        }
    )

def framework(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/framework.html',
        {
            'title':'Framework',
            'message':'HIC Group Project',
            'year':datetime.now().year,
        }
    )
