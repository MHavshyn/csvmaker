from accounts.models import User

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, CheckboxInput, Form, fields  # noqa


class AccountCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'password1', 'password2', 'email'] # noqa
