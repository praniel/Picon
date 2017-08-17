from django.conf.urls import url
from . import views
from picon import settings
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/',views.login, name='login'),
    # url(r'^register/',views.register, name='register'),
    url(r'^register/',views.register, name='register'),
    url(r'^sign_up', views.inputs, name='sign_up'),
    url(r'^sign_in', views.linputs, name='sign_in')
]