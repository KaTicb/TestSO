from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('The email field empty!')
        if not username:
            raise ValueError('The username field empty!')
        if not password:
            raise ValueError('The password field empty!')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=30)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email', 'phone_number']


class Customer(User):
    Company = models.CharField(max_length=30, blank=True, null=True)


class Employee(User):
    position = models.CharField(max_length=30, blank=True, null=True)


class Task(models.Model):
    STATUS_CHOICES = (
        ('waiting_for_executor', 'Waiting for executor'),
        ('in_progress', 'In progress'),
        ('completed', 'Completed'),
    )

    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    close_date = models.DateTimeField(null=True, blank=True, default=None)
    report = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='waiting_for_executor')

    def __str__(self):
        return self.title
