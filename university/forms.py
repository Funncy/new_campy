from django import forms

from .models import University, Department, Community


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

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "college_name", "same_department", "community"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'style': 'width:100%;',
                                           'placeholder': '학과 입력해주세요.'}),
            'college_name': forms.TextInput(attrs={'class': 'form-control',
                                           'style': 'width:100%;',
                                           'placeholder': '단과대학 입력해주세요.'}),
            'same_department': forms.Select(attrs={'class': 'form-control select2',
                                                  'style': 'width:100%;'}),
            'community': forms.Select(attrs={'class': 'form-control select2',
                                                   'style': 'width:100%;'})
        }

    def __init__(self, *args, **kwargs):
        university = kwargs.pop('university', None)
        super().__init__(*args, **kwargs)
        self.fields['same_department'].choices = [('', '없음')]
        #for department in Department.objects.filter(university=university):
        #    if self.initial['name'] != department.name:
        #        self.fields['same_department'].choices += (department.id, department.college_name + ' : ' + department.name)
        self.fields['same_department'].choices += [(u.id, u.college_name + ' : ' + u.name) for u in
                                                  Department.objects.filter(university=university)]
        self.fields['same_department'].initial = None

        self.fields['community'].choices = [(u.id, u.name) for u in
                                                   Community.objects.all()]
