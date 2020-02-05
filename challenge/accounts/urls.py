from django.urls import path, include

from . import views
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()

router.register(r'accounts', views.AccountViewSet)

urlpatterns = router.urls
