from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models


from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Введите электронную почту",
    )

    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        **NULLABLE,
    )
    city = models.CharField(
        max_length=50, verbose_name="Город", help_text="Укажите город", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        help_text="Добавьте аватар",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):

    PAYMENT_CHOICE = [
        ("cash", "наличные"),
        ("transfer", "перевод на счет"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
    )
    payment_date = models.DateField(
        default=date.today, verbose_name="Дата оплаты", **NULLABLE
    )

    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE
    )
    amount_payment = models.PositiveIntegerField(
        verbose_name="Cумма оплаты", help_text="Укажите сумму оплаты", **NULLABLE
    )

    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_CHOICE,
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
    )

    session_id = models.CharField(
        max_length=255,
        verbose_name="ID сессии",
        **NULLABLE
    )

    link = models.URLField(
        max_length=400,
        verbose_name="Ссылка на оплату",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.user} - {self.amount_payment}"
