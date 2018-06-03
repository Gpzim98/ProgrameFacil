from django.forms import ModelForm
from core.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'texto']
