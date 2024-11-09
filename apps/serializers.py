from rest_framework import serializers
from .models import User, Admin, Staff, Student, Room, Course, Group, StudentProfile, Payment, Salary, Debtor, \
    SkippedClass, DashboardMetrics


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'phone_number', 'branch', 'photo']


class AdminModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'role', 'phone_number', 'branch', 'photo']


class StaffModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'role', 'phone_number', 'branch', 'photo']


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'role', 'phone_number', 'branch', 'photo']


class RoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'capacity', 'resources']


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'course_type', 'price', 'description']


class GroupModelSerializer(serializers.ModelSerializer):
    teacher = StaffModelSerializer()
    room = RoomModelSerializer()
    course = CourseModelSerializer()

    class Meta:
        model = Group
        fields = ['id', 'name', 'teacher', 'day', 'room', 'start_date', 'end_date', 'start_time', 'course']


class StudentProfileModelSerializer(serializers.ModelSerializer):
    user = StudentModelSerializer()
    group = GroupModelSerializer()

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'group', 'balance', 'is_active']


class PaymentModelSerializer(serializers.ModelSerializer):
    student = StudentProfileModelSerializer()

    class Meta:
        model = Payment
        fields = ['id', 'student', 'amount', 'date', 'description']


class SalaryModelSerializer(serializers.ModelSerializer):
    staff = StaffModelSerializer()

    class Meta:
        model = Salary
        fields = ['id', 'staff', 'amount', 'month', 'is_paid']


class DebtorModelSerializer(serializers.ModelSerializer):
    student = StudentProfileModelSerializer()

    class Meta:
        model = Debtor
        fields = ['id', 'student', 'amount_due', 'comments']


class SkippedClassModelSerializer(serializers.ModelSerializer):
    student = StudentProfileModelSerializer()
    group = GroupModelSerializer()

    class Meta:
        model = SkippedClass
        fields = ['id', 'student', 'group', 'date']


class DashboardMetricsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardMetrics
        fields = ['id', 'staff_count', 'active_students_count', 'group_count', 'debtor_count', 'monthly_payment_count',
                  'group_leave_count']
