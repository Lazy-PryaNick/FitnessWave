from django import forms
from .models import ContactProfile

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length = 100, required = False, help_text = "100 char max")
    email = forms.EmailField(max_length = 254, required = True)
    message = forms.CharField(required = True, widget = forms.Textarea)
    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message',)