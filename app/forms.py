from email.policy import default
from django import forms


class ShortItForm(forms.Form):
    url = forms.URLField(label="url", required=True)
    custom_text = forms.CharField(
        label="custom_text", required=False)
    expire = forms.CharField(
        label="Expire",
        widget=forms.NumberInput(),
        required=False
    )
