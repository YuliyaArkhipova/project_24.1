from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

from django.urls import path

from users.views import UserCreateAPIView, PaymentsListAPIView, PaymentCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("payments/", PaymentsListAPIView.as_view(), name="payments_list"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("payments/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
]
