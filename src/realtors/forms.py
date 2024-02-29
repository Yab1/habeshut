from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Your Name", "class": "form_input"}
        ),
    )
    email = forms.EmailField(
        label="",
        max_length=100,
        widget=forms.EmailInput(
            attrs={"placeholder": "Your Email", "class": "form_input"}
        ),
    )
    subject = forms.CharField(
        label="",
        max_length=300,
        widget=forms.TextInput(
            attrs={"placeholder": "Subject", "class": "form_input col-span-full"}
        ),
    )
    message = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={"placeholder": "Message", "class": "form_input col-span-full"}
        ),
    )
