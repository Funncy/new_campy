from django import forms

from .models import SubjectGroup
from university.models import CompletionDivision

class SubjectGroupForm(forms.ModelForm):
    completion_divisions = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                          queryset=CompletionDivision.objects.filter(university=1))

    class Meta:
        model = SubjectGroup
        fields = ["name", "completion_divisions"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                            'style': 'width:100%;',
                                            'placeholder': '과목그룹 이름을 입력해주세요.'})
        }

    def __init__(self, *args, **kwargs):
        university = kwargs.pop('university', None)
        super().__init__(*args, **kwargs)
        #for department in Department.objects.filter(university=university):
        #    if self.initial['name'] != department.name:
        #        self.fields['same_department'].choices += (department.id, department.college_name + ' : ' + department.name)
        self.fields['completion_divisions'].choices = [(u.id, u.name) for u in
                                                   CompletionDivision.objects.filter(university=1)]
