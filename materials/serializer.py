from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validators import VideoValidators


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()
    lessons = SerializerMethodField()
    subscriptions = SerializerMethodField()

    def get_count_lesson(self, obj):
        return Lesson.objects.filter(course=obj.id).count()

    def get_lessons(self, obj):
        return [lesson.name for lesson in Lesson.objects.filter(course=obj)]

    def get_subscriptions(self, obj):
        user = self.context["request"].user
        return Subscription.objects.all().filter(user=user, course=obj).exists()

    class Meta:
        model = Course
        fields = (
            "name",
            "description",
            "count_lesson",
            "lessons",
            "subscriptions",
        )


class LessonSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [VideoValidators(field="link_video")]


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
