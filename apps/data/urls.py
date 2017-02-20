from django.conf.urls import url

from .views import home, clean

app_name = 'data'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^clean/$', clean, name='clean'),
]
