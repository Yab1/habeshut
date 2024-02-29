from django import forms


class AgentForm(forms.Form):
    name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Name", "class": "form_input"}),
    )
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form_input"}),
    )
    nessage = forms.CharField(
        label="",
        max_length=500,
        widget=forms.Textarea(attrs={"placeholder": "Message", "class": "form_input"}),
    )
