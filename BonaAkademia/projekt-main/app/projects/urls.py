from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='Project')
router.register(r'projects-shortlist', views.ProjectShortViewSet, basename='Project-Shortlist')
router.register(r'clients', views.ClientViewSet, basename='Client')

urlpatterns = [
    path('', include(router.urls)),
]
