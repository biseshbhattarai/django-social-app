from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['status', 'upload_image', 'user']