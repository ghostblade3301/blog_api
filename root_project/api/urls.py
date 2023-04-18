# urls.py
from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import PostViewSet

router = DefaultRouter()
router.register('v1/posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]