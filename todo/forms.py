from django import forms
from .models import task
class todolistForm(forms.ModelForm):
	class Meta:
		model=task
		fields=["item","complete"]
