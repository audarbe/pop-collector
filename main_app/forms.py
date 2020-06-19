from django.forms import ModelForm
from .models import Limited

class LimitedForm(ModelForm):
    class Meta:
        model = Limited
        fields = ['name', 'typeOfVariant']