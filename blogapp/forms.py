from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cat, Post

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = {
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        }
        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = cleaned_data['first_name']
            user.last_name = cleaned_data['last_name']
            user.email = cleaned_data['email']

            if commit:
                user.save()

            return user

class CatCreationForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = {'name',
                  'years',
                  'breed',
                  'img'}
        def save(self, commit=True):
            cat = super(RegistrationForm, self).save(commit=False)
            cat.name = cleaned_data['name']
            cat.years = cleaned_data['years']
            cat.breed = cleaned_data['breed']
            cat.img = cleaned_data['img']

            if commit:
                cat.save()

            return cat

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'name','email','subject','message'}


