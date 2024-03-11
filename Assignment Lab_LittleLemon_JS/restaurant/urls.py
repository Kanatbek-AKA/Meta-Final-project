from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)


app_name = "restaurant"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),
    path("reservations/", views.reservations, name="reservations"),
    path("menu/", views.menu, name="menu"),
    path("menu_item/<int:pk>/", views.display_menu_item, name="menu_item"),
    path("bookings", views.bookings, name="bookings"),
    # # just type users/, users/me, token/login/
    path("auth/create/", TokenObtainPairView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path("auth/verify/", TokenVerifyView.as_view()),
    path("auth/blacklist/", TokenBlacklistView.as_view()),
    # Api view
    path("api/bookings/", views.BookView.as_view()),
    path("api/registration/", views.Registration.as_view()),
    path("api/menu/", views.MenuItemsView.as_view()),
    path("api/menu/<int:pk>", views.SingleMenuItemView.as_view()),
]
