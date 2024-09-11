from django import forms
from .models import (
    Student, GeneralInformation, LearningProfile, DevelopmentalArea,
    SkillsStrengths, AccessibleLearningSupport, Goal, InterventionService,
    SupplementaryService, ICPParticipant, ImportantDates
)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'id_card_number', 'ie_program', 'date_of_document']

class GeneralInformationForm(forms.ModelForm):
    class Meta:
        model = GeneralInformation
        exclude = ['student']

class LearningProfileForm(forms.ModelForm):
    class Meta:
        model = LearningProfile
        exclude = ['student']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'others':
                self.fields[field].widget = forms.RadioSelect(choices=LearningProfile.CONDITION_STATUS)

class DevelopmentalAreaForm(forms.ModelForm):
    class Meta:
        model = DevelopmentalArea
        exclude = ['student']

class SkillsStrengthsForm(forms.ModelForm):
    class Meta:
        model = SkillsStrengths
        exclude = ['student']

class AccessibleLearningSupportForm(forms.ModelForm):
    class Meta:
        model = AccessibleLearningSupport
        exclude = ['student']

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        exclude = ['student']

class InterventionServiceForm(forms.ModelForm):
    class Meta:
        model = InterventionService
        exclude = ['student']

class SupplementaryServiceForm(forms.ModelForm):
    class Meta:
        model = SupplementaryService
        exclude = ['student']

class ICPParticipantForm(forms.ModelForm):
    class Meta:
        model = ICPParticipant
        exclude = ['student']

class ImportantDatesForm(forms.ModelForm):
    class Meta:
        model = ImportantDates
        exclude = ['student']
