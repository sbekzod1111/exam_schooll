from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.managers import CustomUserManager


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'

    username = None
    role = models.CharField(max_length=20, choices=Role.choices)
    phone_number = models.CharField(max_length=13, unique=True)
    branch = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)
    balance = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='%Y/%m/%d/', null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.role.capitalize()} - {self.phone_number}"


# Define proxy models for each role
class Admin(User):
    class Meta:
        proxy = True

    @classmethod
    def get_queryset(cls):
        return super().objects.filter(role=User.Role.ADMIN)


class Moderator(User):
    class Meta:
        proxy = True

    @classmethod
    def get_queryset(cls):
        return super().objects.filter(role=User.Role.MODERATOR)


class Teacher(User):
    class Meta:
        proxy = True

    @classmethod
    def get_queryset(cls):
        return super().objects.filter(role=User.Role.TEACHER)


class Student(User):
    class Meta:
        proxy = True

    @classmethod
    def get_queryset(cls):
        return super().objects.filter(role=User.Role.STUDENT)


class Room(models.Model):
    name = models.CharField(max_length=20)
    room_capacity = models.CharField(max_length=10)
    number_of_desks_and_chairs = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    class Type(models.TextChoices):
        ONLINE = 'online', 'Online'
        OFFLINE = 'offline', 'Offline'
        VIDEO_COURSE = 'video course', 'Video course'

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=Type.choices)
    price = models.IntegerField()
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    class Days(models.TextChoices):
        EVEN_DAY = 'even day', 'Even day'
        ODD_DAY = 'odd day', 'Odd day'
        MONDAY = 'monday', 'Monday'
        TUESDAY = 'tuesday', 'Tuesday'
        WEDNESDAY = 'wednesday', 'Wednesday'
        THURSDAY = 'thursday', 'Thursday'
        FRIDAY = 'friday', 'Friday'
        SATURDAY = 'saturday', 'Saturday'

    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    day = models.CharField(max_length=20, choices=Days.choices)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    course_start_date = models.DateField(null=True, blank=True)
    course_end_date = models.DateField(null=True, blank=True)
    course_start_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class SkippedClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Skipped class for {self.student}"


class Debtor(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Debtor: {self.student}"
