from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'make',
            'model',
            'year',
            'color',
        ]

    # Customize field labels if needed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['make'].label = "Car Make"
        self.fields['model'].label = "Car Model"
        self.fields['year'].label = "Year of Manufacture"
        self.fields['color'].label = "Color"
