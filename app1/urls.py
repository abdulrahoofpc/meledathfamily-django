from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home, name='home'),
    path('memory/<int:id>/', views.memory_detail, name='memory_detail'),

    path('premium-events/', views.premium_event_view, name='premium_event_list'),
    path('premium-events/<slug:slug>/', views.premium_event_detail, name='premium_event_detail'),
    
    path('team/', views.team_list, name='team'),
    path('team/<slug:slug>/', views.team_detail, name='team_detail'),

    path('memory', views.Home, name='memory_detail'),
    path('family2/', views.family2, name='family2'),
    # path('family_tree', views.family_tree_view, name='family_tree'),
    path('login/', views.custom_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('discussion/', views.discussion_view, name='discussion'),
    path('post-comment/', views.post_comment, name='post_comment'),
    path('family-pillars/', views.FamilyPillars, name='family_pillars'),
    path('history/', views.History, name='history'),
    path('events/', views.event_list, name='events'),
    path('gallery/', views.gallery_list, name='gallery'),
    path('team/', views.Team, name='team'),
    path('familytree1/', views.FamilyTree1, name='familytree1'),
]

