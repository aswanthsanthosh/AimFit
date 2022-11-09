import re

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from aimfit_app.models import Login, Trainer, Physician, Equipments, Customer, Batch, Complaint, DietPlan, Attendance, \
    HealthCondition, Notification, Payment, Chat


class TimeInput(forms.TimeInput):
    input_type = 'time'


class DateInput(forms.DateInput):
    input_type = 'date'

def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')

def card_no_validator(value):
    if not re.compile(r'^[0-9]\d{11}$').match(value):
        raise ValidationError('This is Not a Valid Credit Card Number')

def cvv_validatior(value):
    if not re.compile(r'^[0-9]\d{2}$').match(value):
        raise ValidationError('this is not a valid cvv')

# class DateInput(forms.DateInput):
#     input_type = 'due_date'

class LoginForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class TrainerForm(forms.ModelForm):
    contact_no=forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Trainer
        fields = ('name', 'age', 'address', 'qualification', 'achievement', 'contact_no', 'image')


class PhysicianForm(forms.ModelForm):
    contact_no=forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Physician
        fields = ('name', 'age', 'address', 'qualification', 'contact_no', 'image')


class EquipmentsForm(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = ('name', 'image', 'discrition')


class CustomerForm(forms.ModelForm):
    contact_no=forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Customer
        fields = ('name', 'age', 'address', 'contact_no', 'image')


class BatchForm(forms.ModelForm):
    time: forms.TimeInput(attrs={'type': 'time'})

    class Meta:
        model = Batch
        fields = ('name', 'time')


class ComplaintForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Complaint
        fields = ('complaint', 'date')


class DietForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ('heading', 'diet')


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('attendance', 'date', 'time')


class HealthForm(forms.ModelForm):
    class Meta:
        model = HealthCondition
        fields = ('name', 'height', 'weight', 'medicinconsumption')


class NotificationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Notification
        fields = ('date', 'subject', 'text')


class PaymentForm(forms.ModelForm):
    due_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Payment
        fields = ('name', 'amount', 'due_date')


class ChatForm(forms.ModelForm):
    class Meta:
        model=Chat
        fields=('message',)