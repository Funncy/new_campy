from django import forms
from .models import StudentInfo
from university.models import University, Department
from django.forms import ModelChoiceField

class StudentForm(forms.ModelForm):
    university = forms.ModelChoiceField(queryset=University.objects.all(), initial=1,
                                        widget=forms.Select(attrs={
                                            'class':'form-control select2',
                                            'style': 'width:100%;',
                                            'id' : 'form_university'},))
    major = forms.ModelChoiceField(queryset=Department.objects.filter(university=1), initial=1,
                                   widget=forms.Select(attrs={
                                       'class': 'form-control select2',
                                       'style': 'width:100%;',
                                       'id': 'form_major'}, )
                                   )

    sub_major = forms.ModelChoiceField(queryset=Department.objects.filter(university=1), initial=None,
                                   widget=forms.Select(attrs={
                                       'class': 'form-control select2',
                                       'style': 'width:100%;',
                                       'id': 'form_sub_major'}, )
                                   )

    multi_major = forms.ModelChoiceField(queryset=Department.objects.filter(university=1), initial=None,
                                       widget=forms.Select(attrs={
                                           'class': 'form-control select2',
                                           'style': 'width:100%;',
                                           'id': 'form_multi_major'}, )
                                       )

    admission_year = forms.IntegerField(widget=forms.Select(attrs={
                                           'class': 'form-control select2',
                                           'style': 'width:100%;',
                                           'id': 'form_multi_major'}, ))

    class Meta:
        model = StudentInfo
        fields = ["university", "major", "sub_major", "multi_major", "admission_year"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['university'].choices = [(u.id, u.name) for u in University.objects.all()]
        self.fields['major'].choices = [(u.id, u.college_name + ' : ' + u.name) for u in
                                        Department.objects.filter(university=1)]

        self.fields['multi_major'].choices = [('', '없음')]
        self.fields['multi_major'].choices += [(u.id, u.college_name + ' : ' + u.name) for u in
                                        Department.objects.filter(university=1)]
        self.fields['multi_major'].initial = None

        self.fields['sub_major'].choices = [('', '없음')]
        self.fields['sub_major'].choices += [(u.id, u.college_name + ' : ' + u.name) for u in
                                             Department.objects.filter(university=1)]
        self.fields['sub_major'].initial = None