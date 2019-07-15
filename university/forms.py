from django import forms

from .models import University


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ["name", "maximum_credit"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                            'style': 'width:100%;',
                                            'placeholder': '대학이름을 입력해주세요.'}),
            'maximum_credit': forms.Select(attrs={'class': 'form-control select2',
                                                  'style': 'width:100%;'},)
        }
