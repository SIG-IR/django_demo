from django.conf.urls import url

from . import views

urlpatterns = [
    # Relative url - so it's really going to the parent url in electionsite/urls.py first, then coming here
    url(r'^$', views.index, name='index'),
    url(r'^states/(?P<state>\w+)/$', views.state, name='state'),
]