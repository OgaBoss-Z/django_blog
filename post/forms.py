from django import forms
#from .models import Comment


class CommentForm(forms.Form):
   body = forms.CharField(widget=forms.Textarea(attrs={
      'class': 'form-control input-mf',
      'placeholder': 'Leave a comment',
      'rows': 4
   }))
