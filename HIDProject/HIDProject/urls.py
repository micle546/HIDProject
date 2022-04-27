"""
Definition of urls for HIDProject.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('reptiles/', views.reptiles, name='reptiles'),
    path('birds/', views.birds, name='birds'),
    path('amphibians/', views.amphibians, name='amphibians'),
    path('mammals/', views.mammals, name='mammals'),
    path('fish/', views.fish, name='fish'),
    path('invertebrates/', views.invertebrates, name='invertebrates'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('framework/', views.framework, name='framework'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
