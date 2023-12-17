from django import forms
from .models import BlogPost, Comment,Rating
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RatingForm(forms.ModelForm):
    direct_input = forms.IntegerField(
        label='Direct Input (1-5)',
        min_value=1,
        max_value=5,
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Rating
        fields = ['value']
        widgets = {
            'value': forms.RadioSelect(attrs={'class': 'rating-input'}),
        }
