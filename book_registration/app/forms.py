from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['book_name','author','genere','language','image']
		widgets={
		'book_name':forms.TextInput(attrs={'class':'form-control'}),
		'author':forms.TextInput(attrs={'class':'form-control'}),
		'genere':forms.TextInput(attrs={'class':'form-control'}),
		'language':forms.TextInput(attrs={'class':'form-control'})
		}