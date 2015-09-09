from django.conf.urls import *
from petvs.views import startVS, rank

urlpatterns = [
    url(r'^$', startVS),
    url(r'^rank/$', rank),
]