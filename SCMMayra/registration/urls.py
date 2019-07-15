from django.urls import path
from .views import SignUpView
from . import views

urlpatterns=[
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login_success/', views.login_success, name="login_success"),
    path('logout_success/', views.logout_success, name="logout_success"),
]
