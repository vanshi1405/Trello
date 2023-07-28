from datetime import datetime
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


priority = [
    ("High", "High"),
    ("Medium", "Medium"),
    ("Low", "Low"), ]
status = [
    ("ToDo", "ToDo"),
    ("Done", "Done"),
    ("Doing", "Doing"), ]
company_size = [
    ("1-50", "1-50"),
    ("50-100", "50-100"),
    ("100+", "100+"), ]

job_profile = [
    ("Frontend developer", "Frontend developer"),
    ("Backtend developer", "FBackend developer"),
    ("Support Engineer", "Support Engineer"), ]


def validate_mobile_number(value):
    mobile_number_str = str(value)
    if len(mobile_number_str) != 10:
        raise models.ValidationError("mobile number contains 10 digit ")
    return value


def present_or_future_date(value):
    if value < datetime.date.today():
        raise models.ValidationError("The date cannot be in the past!")
    return value


class Organization(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_number = models.BigIntegerField(validators=[validate_mobile_number])
    stack = models.CharField(max_length=20)
    company_size = models.CharField(choices=company_size, max_length=10)

    def __str__(self):
        return self.name


class Location(models.Model):
    organization = models.ForeignKey(Organization, related_name="locations", on_delete=models.CASCADE)
    country = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    address1 = models.CharField(max_length=30)


class Board(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, related_name="boards", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Member(User):
    mobile_number = models.BigIntegerField(validators=[validate_mobile_number])
    dob = models.DateField()
    job_profile = models.CharField(choices=job_profile, max_length=30)
    image = models.ImageField()
    board = models.ManyToManyField(Board, related_name='members')

    def __str__(self):
        return self.first_name


class Card(models.Model):
    user = models.ForeignKey(Member, related_name='cards', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='cards_on_board', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    start_date = models.DateField(validators=[present_or_future_date])
    due_date = models.DateField(validators=[present_or_future_date])
    status = models.CharField(choices=status, max_length=10)
    priority = models.CharField(choices=priority, max_length=10)
    lable = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Checklist(models.Model):
    card = models.ForeignKey(Card, related_name='checklist', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
