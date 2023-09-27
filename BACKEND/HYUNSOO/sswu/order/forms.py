from django import forms
from .models import Reservation, DATE_CHOICES

class ReservationForm(forms.ModelForm):
    purchase_date = forms.ChoiceField(
        choices=DATE_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Reservation
        fields = ['user_name', 'phone_number', 'user_mail', 'purchase_date', 'purchase_time']
 