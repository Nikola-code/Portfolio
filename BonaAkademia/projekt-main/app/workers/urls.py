from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'workers', views.WorkerViewSet)
router.register(r'weeks', views.WeekViewSet)
router.register(r'jobtimes', views.JobTimeViewSet)
router.register(r'workers-availability', views.WorkerAvailabilityViewSet)
router.register(r'planning/week/(?P<week_id>\d+)', views.PlanningViewSet, basename = 'Planning')

urlpatterns = [
    path('', include(router.urls)),
    path(r'workers-create/', views.WorkerList.as_view()),
    path(r'workers-edit/<int:pk>/', views.WorkerDetail.as_view()),
    path(r'weeks-years/<int:pk>/', views.WeekList.as_view()),
    path(r'jobtime-availability/<int:pk>/', views.JobTimeAvailabilityDetail.as_view()),
    path(r'workers-projects/<int:pk>/', views.WorkerProjectsDetail.as_view())
]
