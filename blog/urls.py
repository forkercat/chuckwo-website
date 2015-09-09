from django.conf.urls import *
from blog.views import archive, iosapi


urlpatterns = [
    url(r'^$', archive),
    url(r'^blog.json$', iosapi),
    url(r'^tinymce/', include('tinymce.urls')),
]