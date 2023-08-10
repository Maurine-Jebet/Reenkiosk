from django import forms

from .models import Buyer

class CustomerUploadForm(forms.ModelForm):
    class Meta:
        model=Buyer
        fields= "__all__"