from django.urls import path
from rest_framework import routers
from . import views
app_name = 'eapi'
router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)

router.register('club', views.ClubViewSet, basename='create')


urlpatterns = router.urls
