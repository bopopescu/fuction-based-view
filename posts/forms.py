from django import forms
from .models import Post


# class DateInput(forms.DateInput):
#     input_type = 'date'

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
