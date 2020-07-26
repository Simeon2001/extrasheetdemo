from django.urls import path
from . import views
from .views import RegisterView,LoginView,ProfilesCreateView,ClubCreateView

urlpatterns = [
    path ('', views.index, name = 'Home/' ),
    path ('club/' ,views.club_view, name = 'clubl'),
    path ('clubs/<str:pi>/' ,views.clubs, name = 'clubs'),
    path ('forum/<str:pi>/' ,views.club_forum, name = 'forum'),
    path ('insight/<str:pi>/' ,views.club_insight, name = 'insight'),
    path ('join/' ,views.join_club, name = 'join_club'),
    path ('club-join/' ,views.club_join, name = 'club-join'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', ProfilesCreateView.as_view(), name='profile'),
    path('create-club/',ClubCreateView.as_view(),name='club'),
    
]