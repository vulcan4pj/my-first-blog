from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^accounts/login/',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={ 
            'template_name' : 'login.html'
        }
    ),
    url(
        r'^accounts/logout/',
        'django.contrib.auth.views.logout',
        name='logout',
    ),
    url(
        r'^$', 
        views.main, 
        name='main'
    ),
]