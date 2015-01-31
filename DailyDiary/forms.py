from django import forms
from DailyDiary.models import Post

class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post

