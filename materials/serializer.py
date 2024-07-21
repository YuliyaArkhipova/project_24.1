from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_count_lesson(self, obj):
        return Lesson.objects.filter(course=obj.id).count()

    def get_lessons(self, obj):
        return [lesson.name for lesson in Lesson.objects.filter(course=obj)]

    class Meta:
        model = Course
        fields = (
            "name",
            "description",
            "count_lesson",
            "lessons",
        )


class LessonSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"
