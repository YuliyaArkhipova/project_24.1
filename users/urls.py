from users.apps import UsersConfig

from django.urls import path

from users.views import UserCreateAPIView, PaymentsListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user_list'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
]
