from django.urls import path, include

from rest_framework import routers
from . import apiviews

router = routers.DefaultRouter()
router.register(r'users', apiviews.UserViewSet)
router.register(r'groups', apiviews.GroupViewSet)

from .views import index

urlpatterns = [
    path("", index),
    path('api/', include(router.urls)),
]