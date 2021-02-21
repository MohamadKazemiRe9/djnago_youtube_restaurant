from django import forms
from .models import Reseravtion

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reseravtion
        fields = "__all__"