
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)  # Ensure this field is set as required
    message = forms.CharField(widget=forms.Textarea, required=True)





