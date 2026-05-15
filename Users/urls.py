from .views.login_view import LoginView
from django.urls import path
from .views.register_view import RegisterView
from Users.views.profile_view import ProfileView
from Users.views.public_profile_view import PublicProfileView
from Users.views.verificar_email_view import VerifyEmailView
from Users.views.verificar_view import VerifyCodeView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('public-profile/<str:email>/', PublicProfileView.as_view()),
    path('verify-email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='public-profile'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify-code'),
]