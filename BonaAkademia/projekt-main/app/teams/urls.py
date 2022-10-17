from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'teams-list', views.TeamListViewSet)
router.register(r'teams-members', views.TeamMembersViewSet)
router.register(r'teams-workers', views.TeamWorkerViewSet)
router.register(r'teams-leaders', views.TeamLeaderViewSet)
router.register(r'teams-membership', views.TeamMembershipViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('teams-creation/', views.TeamList.as_view()),
	path('teams-creation/<int:pk>/', views.TeamDetail.as_view())
]

