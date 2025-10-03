from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path("contact/", views.contact, name="contact"),
    path("user-form/", views.user_form, name="user_form"),
    path("users/", views.user_list, name="user_list"),
    path("users/delete/<int:pk>/", views.user_delete, name="user_delete"),
    path('users/update/<int:pk>/', views.user_update, name='user_update'),
    path("products/", views.product_list, name="product_list"),
    path("signup/", views.signup, name="signup"),
]



