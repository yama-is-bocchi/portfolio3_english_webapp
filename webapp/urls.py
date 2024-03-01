from django.urls import path
from webapp import views

app_name = 'webapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/setting/', views.setting_page, name='setting_page'),
    path('index/setting/add/', views.add_word_page, name='add_word_page'),
    path('index/setting/edit/', views.edit_word_page, name='edit_word_page'),
    path('update/setting/edit/<int:pk>/', views.updateword, name='updateword'),
    path('delete/setting/edit/<int:pk>/', views.deleteword, name='deleteword'),
    path('index/setting/view/', views.view_word_page, name='view_word_page'),
    path('index/game/', views.start_game, name='start_game'),
    path('index/game2/', views.start_eng_game, name='start_eng_game'),
]