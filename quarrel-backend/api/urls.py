from django.urls import path, include
from . import views

urlpatterns = [
    # Authentication URLs
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('passwordReset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # User URLs
    path('user/', views.user_store),
    path('userCreate/', views.user_create),

    # Ping!
    path('', views.ping),

    # Game URLs
    path('chooseWord/', views.choose_word),
    path('getWords/', views.choose_word),
    path('isWordValid/', views.is_word_valid),
    path('normalGame/', views.normal_game),
    path('getPreviousGameData/', views.get_previous_game_data),
    path('rankedGame/', views.ranked_game),

    path('startWebsocket/', views.start_websocket)
]
