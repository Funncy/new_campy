from django import forms

from .models import SubjectGroup, RuleGeneral, RuleSpecific
from university.models import CompletionDivision, Track

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
        # 자신을 뺀 이수구분을 목록에 넣기 (오류로 보류)
        #for department in Department.objects.filter(university=university):
        #    if self.initial['name'] != department.name:
        #        self.fields['same_department'].choices += (department.id, department.college_name + ' : ' + department.name)
        self.fields['completion_divisions'].choices = [(u.id, u.name) for u in
                                                   CompletionDivision.objects.filter(university=1)]

class RuleGeneralForm(forms.ModelForm):

    value = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'width:100%;'}))

    class Meta:
        model = RuleGeneral
        fields = ['name', 'track', 'type', 'value', 'subject_group']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'style': 'width:100%;',
                                           'placeholder': '과목그룹 이름을 입력해주세요.'}),
            'track': forms.Select(attrs={'class': 'form-control select2',
                                         'style': 'width:100%;'}),
            'type': forms.Select(attrs={'class': 'form-control select2',
                                         'style': 'width:100%;'}),
            'subject_group': forms.Select(attrs={'class': 'form-control select2',
                                         'style': 'width:100%;'}),
        }

    def __init__(self, *args, **kwargs):
        university = kwargs.pop('university', None)
        super().__init__(*args, **kwargs)
        # track, subject_group 대학 소속 데이터 불러오기

        self.fields['track'].choices = [(u.id, u.name) for u in
                                        Track.objects.filter(university=university)]
        self.fields['subject_group'].choices = [(u.id, u.name) for u in
                                        SubjectGroup.objects.filter(university=university)]


class RuleSpecificForm(forms.ModelForm):

    value = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'width:100%;'}))

    class Meta:
        model = RuleSpecific
        fields = ['name', 'track', 'type', 'value', 'subject_group', 'upper_rule', 'change_rule']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'style': 'width:100%;',
                                           'placeholder': '과목그룹 이름을 입력해주세요.'}),
            'track': forms.Select(attrs={'class': 'form-control select2',
                                         'style': 'width:100%;'}),
            'type': forms.Select(attrs={'class': 'form-control select2',
                                        'style': 'width:100%;'}),
            'subject_group': forms.Select(attrs={'class': 'form-control select2',
                                                 'style': 'width:100%;'}),
            'upper_rule': forms.Select(attrs={'class': 'form-control select2',
                                                 'style': 'width:100%;'}),
            'change_rule': forms.Select(attrs={'class': 'form-control select2',
                                              'style': 'width:100%;'}),
        }

    def __init__(self, *args, **kwargs):
        university = kwargs.pop('university', None)
        year = kwargs.pop('year', None)
        department = kwargs.pop('department', None)
        super().__init__(*args, **kwargs)
        # track, subject_group 대학 소속 데이터 불러오기

        self.fields['track'].choices = [(u.id, u.name) for u in
                                        Track.objects.filter(university=university)]
        self.fields['subject_group'].choices = [(u.id, u.name) for u in
                                        SubjectGroup.objects.filter(university=university)]
        self.fields['upper_rule'].choices = [(None, '없음')]
        self.fields['upper_rule'].choices += [(u.id, u.track.name + ' : ' + u.name) for u in
                                                RuleGeneral.objects.filter(university=university)]
        self.fields['change_rule'].choices = [(None, '없음')]
        self.fields['change_rule'].choices += [(u.id, u.track.name + ' : ' + u.name) for u in
                                              RuleSpecific.objects.filter(university=university,
                                                                          department=department,
                                                                          year=year)]