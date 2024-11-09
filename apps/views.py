from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from apps.models import User, Admin, Staff, Student, Room, Course, Group, StudentProfile, Payment, Salary, Debtor, \
    SkippedClass, DashboardMetrics
from apps.serializers import (
    UserModelSerializer, AdminModelSerializer, StaffModelSerializer, StudentModelSerializer,
    RoomModelSerializer, CourseModelSerializer, GroupModelSerializer, StudentProfileModelSerializer,
    PaymentModelSerializer, SalaryModelSerializer, DebtorModelSerializer, SkippedClassModelSerializer,
    DashboardMetricsModelSerializer
)


# User Views
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


# Admin Views
class AdminListAPIView(ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminModelSerializer


class AdminCreateAPIView(CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminModelSerializer


# Staff Views
class StaffListAPIView(ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffModelSerializer


class StaffCreateAPIView(CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffModelSerializer


# Student Views
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# Room Views
class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer


# Course Views
class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer


class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer


# Group Views
class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


class GroupCreateAPIView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


class GroupRetrieveAPIView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


class GroupUpdateAPIView(UpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


class GroupDestroyAPIView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


# Student Profile Views
class StudentProfileListAPIView(ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileModelSerializer


class StudentProfileCreateAPIView(CreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileModelSerializer


# Payment Views
class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer


class PaymentCreateAPIView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer


# Salary Views
class SalaryListAPIView(ListAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalaryModelSerializer


class SalaryCreateAPIView(CreateAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalaryModelSerializer


# Debtor Views
class DebtorListAPIView(ListAPIView):
    queryset = Debtor.objects.all()
    serializer_class = DebtorModelSerializer


class DebtorCreateAPIView(CreateAPIView):
    queryset = Debtor.objects.all()
    serializer_class = DebtorModelSerializer


# Skipped Class Views
class SkippedClassListAPIView(ListAPIView):
    queryset = SkippedClass.objects.all()
    serializer_class = SkippedClassModelSerializer


class SkippedClassCreateAPIView(CreateAPIView):
    queryset = SkippedClass.objects.all()
    serializer_class = SkippedClassModelSerializer


# Dashboard Metrics Views
class DashboardMetricsRetrieveAPIView(RetrieveAPIView):
    queryset = DashboardMetrics.objects.all()
    serializer_class = DashboardMetricsModelSerializer
