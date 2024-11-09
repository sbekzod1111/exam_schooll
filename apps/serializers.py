from rest_framework.serializers import ModelSerializer

from apps.models import Group, SkippedClass, Room, User, Course


class GroupModelSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = 'id', 'name', 'teacher', 'course_start_time', 'day'

    def to_representation(self, instance):
        return super().to_representation(instance)


class GroupCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = 'name', 'teacher', 'day', 'room', 'course_start_time'


class SkippedClassModelSerializer(ModelSerializer):
    class Meta:
        model = SkippedClass
        fields = 'student', 'group'


class RoomModelSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = 'name', 'room_capacity', 'number_of_desks_and_chairs'


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'phone_number', 'role'


class UserCreateModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'phone_number', 'role', 'date_of_birth', 'gender', 'photo'


class UserRetrieveUpdateDestroyModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'photo', 'balance', 'role', 'branch'


class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
