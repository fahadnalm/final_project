from django.urls import include, path
from story import views


app_name = 'story'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('about_game/', views.about_game, name='about_game'),
    path('start/', views.start, name='start'),
    path('next/<str:user_choice>/<int:next_page>/', views.next_page, name='next'),
]
