from django.urls import path
from . import views, views_ajax

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<category_name_slug>', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<category_name_slug>/add_page/', views.add_page, name='add_page'),
    #path('register/', views.register, name='register'),
    #path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    #path('logout/', views.user_logout, name='logout'),
    #path('search/', views.search, name='search'),
    path('goto/', views.track_url, name='goto'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/<username>', views.profile, name='profile'),
    path('profiles/', views.list_profiles, name='list_profiles'),
    path('like/', views.like_category, name='like_category'),
    path('add_page_button/', views.add_page_button, name='add_page_button'),
    path('suggest/', views.suggest_category, name='suggest_category'),
]
