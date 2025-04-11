from django import forms
from apps.galery.models import Image

class ImageForms(forms.ModelForms):
    class Meta:
        model = Image
        exclude = ['published',]

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'caption': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'photograph': forms.FileInput(attrs={'class':'form-control'}),
            'date_photograph': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'user': forms.Select(attrs={'class':'form-control'}),
        }