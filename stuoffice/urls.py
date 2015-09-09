from django.conf.urls import *
from .views import feedbackRecieve

urlpatterns = [
    url(r'^feedback.json$', feedbackRecieve),
]
