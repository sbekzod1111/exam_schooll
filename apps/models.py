from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'
        STUDENT = 'student', 'Student'

    username = None
    role = models.CharField(max_length=20, choices=Role.choices)
    phone_number = models.CharField(max_length=13, unique=True)
    branch = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.role.capitalize()} - {self.phone_number}"

    @property
    def is_admin(self):
        return self.role == User.Role.ADMIN

    @property
    def is_staff(self):
        return self.role == User.Role.STAFF

    @property
    def is_student(self):
        return self.role == User.Role.STUDENT


class Admin(User):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = User.Role.ADMIN
        super().save(*args, **kwargs)


class Staff(User):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = User.Role.STAFF
        super().save(*args, **kwargs)


class Student(User):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = User.Role.STUDENT
        super().save(*args, **kwargs)


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    resources = models.TextField(blank=True)  # For desk, chair, projector details

    def __str__(self):
        return self.name


class Course(models.Model):
    class Type(models.TextChoices):
        ONLINE = 'online', 'Online'
        OFFLINE = 'offline', 'Offline'
        VIDEO = 'video', 'Video Course'

    name = models.CharField(max_length=50)
    course_type = models.CharField(max_length=20, choices=Type.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    class Days(models.TextChoices):
        EVEN_DAY = 'even_day', 'Even Day'
        ODD_DAY = 'odd_day', 'Odd Day'
        MONDAY = 'monday', 'Monday'
        TUESDAY = 'tuesday', 'Tuesday'
        WEDNESDAY = 'wednesday', 'Wednesday'
        THURSDAY = 'thursday', 'Thursday'
        FRIDAY = 'friday', 'Friday'
        SATURDAY = 'saturday', 'Saturday'

    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, related_name='teacher_groups')
    day = models.CharField(max_length=20, choices=Days.choices)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='groups')

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.phone_number} - {self.group.name}" if self.group else self.user.phone_number


class Payment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.user.phone_number} - {self.amount} on {self.date}"


class Salary(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='salaries')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.staff.phone_number} - {self.amount} for {self.month}"


class Debtor(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='debts')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.user.phone_number} - Debt: {self.amount_due}"


class SkippedClass(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.phone_number} skipped {self.group.name} on {self.date}"


class DashboardMetrics(models.Model):
    staff_count = models.IntegerField(default=0)
    active_students_count = models.IntegerField(default=0)
    group_count = models.IntegerField(default=0)
    debtor_count = models.IntegerField(default=0)
    monthly_payment_count = models.IntegerField(default=0)
    group_leave_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Dashboard Metric"
        verbose_name_plural = "Dashboard Metrics"

    def __str__(self):
        return "Dashboard Metrics"
