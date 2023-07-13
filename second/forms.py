# from django import forms


#class PostForm(forms.Form):
    # title = forms.CharField(label='제목', max_length=200)
    # CharField => 그냥 입력 박스 나옴, 따라서 긴글 입력하려면  widget=forms.Textarea로 바꿔줘야 함
    # content = forms.CharField(label='내용', widget=forms.Textarea)

from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': _('제목'),
            'content': _('내용'),
        }
        help_text = {
            'title': _('제목을 입력해주세요'),
            'content': _('내용을 입력해주세요'),
        }
        error_message = {
            'name' : {
                'max_length': _("제목이 너무 길어요")
            }
        }
