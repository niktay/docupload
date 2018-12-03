from api import views
from django.conf.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'confidentiality', views.ConfidentialityViewSet)
router.register(r'filetype', views.FileTypeViewSet)

urlpatterns = [url(r'api/', include(router.urls)), ]
