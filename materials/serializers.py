from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Lesson, Course


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()

    def get_lesson_count(self, lesson):
        return Lesson.objects.filter(course=lesson.course).count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'lesson_count',)
