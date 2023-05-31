from django.urls import path
from . import views
#app_name='auction'
from .views import place_bid

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:auction_id>', views.auction_detail, name='auction_detail'),
    path('auction/<int:auction_id>/place_bid/', place_bid, name='place_bid'),

]