#from django import forms
#from django.contrib.auth.models import User
#from laddr_site.models import Profile
#from django.contrib.auth import get_user_model

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length = 254, required = True, widget = forms.EmailInput(), help_text='Required. Please provide a valid email address.')
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = User
