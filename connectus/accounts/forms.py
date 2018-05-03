from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Profile


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        fields = ['address', 'education', 'status', 'user']



    #  address = models.CharField(max_length=120)
    #  gender = models.RadioSelect()
    #  education = models.CharField(max_length=60)
    #  status = models.TextField()
    #  image = models.FileField(upload_to="documents")
     
    #  user = models.OneToOneField(User, on_delete=models.CASCADE)
    #  objects = models.Manager()
