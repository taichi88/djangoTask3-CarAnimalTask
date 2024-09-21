

from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'name',
            'species',
            'age',
            'is_endangered',
        ]

    # Customize field labels if needed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Animal Name"
        self.fields['species'].label = "Species"
        self.fields['age'].label = "Age (Years)"
        self.fields['is_endangered'].label = "Is Endangered?"
