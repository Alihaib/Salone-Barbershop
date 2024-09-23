from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Lecturer
class Signupclient(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class Signupadmin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Loginclient(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1']


from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'service', 'date', 'time', 'comments']
