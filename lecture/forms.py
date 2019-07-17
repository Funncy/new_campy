from django import forms

from university.models import University

class UploadFileForm(forms.Form):
    university = forms.ModelChoiceField(queryset=University.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control select2'}))
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['university'].choices = [(u.id, u.name) for u in
                                                   University.objects.all()]