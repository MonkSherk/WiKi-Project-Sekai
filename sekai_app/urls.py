from django.urls import path, re_path
from sekai_app import views


urlpatterns = [
    path('', views.home, name='home'),

    path('sekai_worlds/', views.SekaiWorldListView.as_view(), name='sekai_world_list'),
    path('sekai_worlds/<int:pk>/', views.SekaiWorldDetailView.as_view(), name='sekai_world_detail'),

    path('groups/', views.GroupListView.as_view(), name='group_list'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),

    path('characters/', views.CharacterListView.as_view(), name='character_list'),
    path('characters/<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),

    path('cards/', views.CardListView.as_view(), name='card_list'),
    path('cards/<int:pk>/', views.CardDetailView.as_view(), name='card_detail'),

    path('songs/', views.SongListView.as_view(), name='song_list'),
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song_detail'),

    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),

    #admins
    path('admin-check/', views.admin_access_check, name='admin_access_check'),
    path('Admins/', views.admin_page, name='admin_page'),
    path('Admins/sekai_worlds/', views.admin_world_list, name='admin_sekai_world_list'),
    path('Admins/characters/', views.admin_character_list, name='admin_character_list'),
    path('Admins/groups/', views.admin_group_list, name='admin_group_list'),
    path('Admins/cards/', views.admin_card_list, name='admin_card_list'),
    path('Admins/songs/', views.admin_song_list, name='admin_song_list'),
    path('Admins/events/', views.admin_event_list, name='admin_event_list'),

    path('sekai_worlds/create/', views.sekai_world_create, name='sekai_world_create'),
    path('sekai_worlds/<int:pk>/update/', views.sekai_world_update, name='sekai_world_update'),
    path('sekai_worlds/<int:pk>/delete/', views.sekai_world_delete, name='sekai_world_delete'),

    path('groups/create/', views.group_create, name='group_create'),
    path('groups/<int:pk>/update/', views.group_update, name='group_update'),
    path('groups/<int:pk>/delete/', views.group_delete, name='group_delete'),

    path('characters/create/', views.character_create, name='character_create'),
    path('characters/<int:pk>/update/', views.character_update, name='character_update'),
    path('characters/<int:pk>/delete/', views.character_delete, name='character_delete'),

    path('cards/create/', views.card_create, name='card_create'),
    path('cards/<int:pk>/update/', views.card_update, name='card_update'),
    path('cards/<int:pk>/delete/', views.card_delete, name='card_delete'),

    path('songs/create/', views.song_create, name='song_create'),
    path('songs/<int:pk>/update/', views.song_update, name='song_update'),
    path('songs/<int:pk>/delete/', views.song_delete, name='song_delete'),

    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:pk>/update/', views.event_update, name='event_update'),
    path('events/<int:pk>/delete/', views.event_delete, name='event_delete'),

    path('sekaiitems/', views.admin_sekai_items_list, name='admin_sekai_items_list'),
    path('sekaiitems/create/', views.admin_sekai_items_create, name='admin_sekai_items_create'),
    path('sekaiitems/<int:pk>/update/', views.admin_sekai_items_update, name='admin_sekai_items_update'),
    path('sekaiitems/<int:pk>/delete/', views.admin_sekai_items_delete, name='admin_sekai_items_delete'),

    re_path(r'^[a-zA-Zа-яА-Я0-9_\-\@\.\+\/]+$', views.custom_404, name='404')
]