from django import forms
from .models import Competitor

class CompetitorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Competitor
        fields = ['full_name', 'age', 'phone_number', 'national_id', 'club_name', 'nationality']