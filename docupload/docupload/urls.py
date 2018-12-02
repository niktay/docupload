from django.conf.urls import include
from django.conf.urls import url

API_TITLE = 'Docupload API'
API_DESCRIPTION = 'REST API for uploading of documents'

urlpatterns = [
    url(r'^', include('api.urls')),
]
