from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название курса", help_text="Укажите название курса"
    )
    preview = models.ImageField(
        upload_to="materials/preview",
        verbose_name="Превью курса",
        help_text="Загрузите превью курса",
        **NULLABLE,
    )
    description = models.TextField(verbose_name="Описание курса", **NULLABLE)
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец курса",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.name}"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Название курса", **NULLABLE)
    name = models.CharField(
        max_length=150,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    description = models.TextField(verbose_name="Описание урока", **NULLABLE)
    preview = models.ImageField(
        upload_to="materials/preview",
        verbose_name="Превью урока",
        help_text="Загрузите превью урока",
        **NULLABLE,
    )
    link_video = models.URLField(
        max_length=255,
        verbose_name="Ссылка на видео",
        help_text="Добавьте ссылку на видео",
        **NULLABLE,
    )

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец урока",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.name}"


class Subscription(models.Model):
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        **NULLABLE)

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Название курса"
    )

    is_subscribe = models.BooleanField(default=False, verbose_name="Подписка")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f"{self.owner} - {self.course}"
