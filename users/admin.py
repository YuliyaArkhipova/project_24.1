from django.contrib import admin

from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "email",
        "phone",
        "city",
        "avatar",

    )


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "payment_date",
        "paid_course",
        "paid_lesson",
        "amount_payment",
        "payment_method",
    )
