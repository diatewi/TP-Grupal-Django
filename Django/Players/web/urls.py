from django.urls import path
from . import views
from .views import GroupsListView, PlayersListView, GroupsCreateView


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('contact', views.contact, name='contact'),
    path('players/League-of-Legends', PlayersListView.as_view(), name='default_nav'),
    path('players/<str:game>/', PlayersListView.as_view(), name='players_list'),
    path('groups/<str:game>/', GroupsListView.as_view(), name='groups_list'),
    path('create-group', views.GroupsCreateView.as_view(), name='create_group'),
    path('update/<pk>', views.GroupsUpdateView.as_view(), name='update_group'),
    path('delete/<pk>', views.GroupsDeleteView.as_view(), name='delete_group'),
]
