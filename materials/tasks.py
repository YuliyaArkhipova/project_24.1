from celery import shared_task
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from materials.models import Subscription


@shared_task
def send_updating_materials_course(course):
    """Отправляет пользователю уведомление об обновлении курса."""
    subscription = Subscription.objects.filter(course=course.id)
    for update in subscription:
        send_mail(
            'Обновление материалов курса',
            f'Материалы курса {update.course.name} обновлены',
            EMAIL_HOST_USER,
            [update.user.email]
        )
