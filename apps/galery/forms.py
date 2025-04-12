from django import forms
from apps.galery.models import Image

class ImageForms(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['published',]
        labels = {
            'name': 'Nome',
            'caption': 'Legenda',
            'category': 'Categoria',
            'description': 'Descrição',
            'photograph': 'Foto',
            'date_photograph': 'Data de Registro',
            'user': 'Usuário'
        }

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