from django.core.paginator import Paginator
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django_flatpickr.schemas import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput

from onlydjango.helpers.cbv import ODCreateView, ODListView, ODUpdateView, ODDeleteView, ODDetailView
from .docgen.icp_generator import ICPDocumentGenerator

from .models import (
    Student, Goal, InterventionService,
    SupplementaryService, GeneralInformation, LearningProfile,
    DevelopmentalArea, SkillsStrengths, AccessibleLearningSupport
)


def home(request):

    icp_obj = Student.objects.all()

    paginator = Paginator(icp_obj, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'icps': page_obj,
    }

    return render(request, 'icp/home.html', context)

class ICPListView(ODListView):
    model = Student
    context_object_name = 'students'
    template_name = 'icp/list.html'

class StudentDetailView(ODDetailView):
    model = Student
    template_name = 'icp/student_detail.html'

class StudentCreateView(ODCreateView):
    model = Student
    fields = ['school_logo', 'name', 'id_card_number', 'age', 'ie_program', 'index', 'date_of_document', 'current_education_level', 'academic_strengths', 'areas_of_interest']
    template_name = 'generic/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Student'
        return context

    def get_form_class(self):
        return modelform_factory(
            self.model,
            fields=self.fields,
            widgets={
                "date_of_document": DatePickerInput(
                    options=FlatpickrOptions(minDate="today"),
                ),
            },
        )

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('general_information', kwargs={'student_id': self.object.id})

class StudentUpdateView(ODUpdateView):
    model = Student
    fields = ['school_logo', 'name', 'id_card_number', 'age', 'ie_program', 'index', 'date_of_document', 'current_education_level', 'academic_strengths', 'areas_of_interest']
    # template_name = 'icp/student_update.html'

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Student'
        return context

    def get_form_class(self):
        return modelform_factory(
            self.model,
            fields=self.fields,
            widgets={
                "date_of_document": DatePickerInput(
                    options=FlatpickrOptions(minDate="today"),
                ),
            },
        )

class StudentDeleteView(ODDeleteView):
    model = Student
    success_url = reverse_lazy('list_icps')

class GeneralInformationView(ODCreateView):
    model = GeneralInformation
    fields = ['parent_concerns', 'medical_alerts']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'General Information'
        return context

    def form_valid(self, form):
        form.instance.student = get_object_or_404(Student, id=self.kwargs['student_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('learning_profile', kwargs={'student_id': self.kwargs['student_id']})

class LearningProfileView(ODCreateView):
    model = LearningProfile
    fields = ['learning_disabilities', 'gifts_and_talents', 'multiple_disabilities', 'physical_impairments', 'hearing_impairments', 'visual_impairments', 'intellectual_impairment', 'autism_spectrum_disorder', 'down_syndrome', 'global_development_delay', 'others']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Learning Profile'
        return context

    def form_valid(self, form):
        form.instance.student = get_object_or_404(Student, id=self.kwargs['student_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('developmental_areas', kwargs={'student_id': self.kwargs['student_id']})

class DevelopmentalAreasView(ODCreateView):
    model = DevelopmentalArea
    fields = [
        'cognitive', 'social_emotional', 'physical', 'language',
        'speaking', 'reading', 'writing', 'listening', 'comprehension', 'others'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Developmental Areas'
        return context

    def form_valid(self, form):
        form.instance.student = get_object_or_404(Student, id=self.kwargs['student_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('skills_strengths', kwargs={'student_id': self.kwargs['student_id']})

class SkillsStrengthsView(ODCreateView):
    model = SkillsStrengths
    fields = [
        'english', 'dhivehi', 'math', 'quran_arabic', 'islam',
        'key_competencies', 'social_skills', 'adaptive_behavior',
        'language_communication', 'others'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Skills & Strengths'
        return context

    def form_valid(self, form):
        form.instance.student = get_object_or_404(Student, id=self.kwargs['student_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accessible_learning_support', kwargs={'student_id': self.kwargs['student_id']})

class AccessibleLearningSupportView(ODCreateView):
    model = AccessibleLearningSupport
    fields = [
        'learning_environment', 'learning_materials', 'adult_support',
        'content', 'methodology', 'assessment_modification'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Accessible Learning Support'
        return context

    def form_valid(self, form):
        form.instance.student = get_object_or_404(Student, id=self.kwargs['student_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('measurable_goals', kwargs={'student_id': self.kwargs['student_id']})

class MeasurableGoalsView(ODCreateView):
    model = Goal
    fields = [
        'area', 'annual_goal', 'assessment_criteria',
        'procedures', 'assessment_schedule', 'responsible_person'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Measurable Goals'
        return context

    def form_valid(self, form):
        form.instance.student = get_object_or_404(Student, id=self.kwargs['student_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('goal_added', kwargs={'student_id': self.kwargs['student_id']})

def goal_added(request, student_id):
    return render(request, 'icp/goal_added.html', {'student_id': student_id})

class InterventionServicesView(ODCreateView):
    model = InterventionService
    fields = [
        'program', 'frequency', 'duration', 'location', 'initiation_date'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Intervention Services'
        return context

    def form_valid(self, form):
        form.instance.student = get_object_or_404(Student, id=self.kwargs['student_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('supplementary_services', kwargs={'student_id': self.kwargs['student_id']})

class SupplementaryServicesView(ODCreateView):
    model = SupplementaryService
    fields = ['type_of_support', 'time', 'duration']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Supplementary Services'
        return context

    def form_valid(self, form):
        form.instance.student = get_object_or_404(Student, id=self.kwargs['student_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('generate_icp', kwargs={'student_id': self.kwargs['student_id']})

def generate_icp(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    generator = ICPDocumentGenerator(student)
    pdf_content = generator.generate()

    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={student.name}_ICP.pdf'

    return response

def icp_success(request):
    return render(request, 'icp/success.html')


