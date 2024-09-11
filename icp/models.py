from django.contrib.auth.models import User
import re

from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# Mainstream Program
# School readiness
# Early intervention
# Homeschooling

def validate_id_card_number(value):
    if not re.match(r'^A\d{1,6}$', value):
        raise ValidationError('ID card number must start with A and be followed by up to 6 digits.')


class Student(models.Model):
    name = models.CharField(max_length=255,
                            help_text="Enter the student's full name as it appears on official documents.")
    id_card_number = models.CharField(max_length=7,
                                      help_text="Enter the student's ID card number for official identification.",
                                      validators=[validate_id_card_number])
    ie_program = models.CharField(max_length=255,
                                  help_text="Specify the Inclusive Education (IE) program the student is enrolled in.",
                                  choices=[('mainstream', 'Mainstream Program'),
                                           ('school_readiness', 'School Readiness'),
                                           ('early_intervention', 'Early Intervention'),
                                           ('homeschooling', 'Homeschooling')])
    date_of_document = models.DateField(
        help_text="Select the date when this ICP document is being created or last updated.")
    current_education_level = models.CharField(max_length=100,
                                               help_text="Indicate the student's current grade level or educational stage.")
    academic_strengths = models.TextField(
        help_text="Describe the student's academic strengths, including subjects or skills where they excel.")
    areas_of_interest = models.TextField(
        help_text="List the student's areas of interest, both academic and non-academic, to help tailor their learning experience.")


class GeneralInformation(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='general_information')
    parent_concerns = models.TextField(
        help_text="Document any concerns expressed by the parents regarding the student's education or development.")
    medical_alerts = models.TextField(
        help_text="List any medical conditions, allergies, or health-related issues that may affect the student's learning or require attention during school hours.")


class StudentEvaluationSummary(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='evaluation_summary')
    diagnosed_conditions = models.TextField(
        help_text="List any officially diagnosed conditions that impact the student's learning, as documented by qualified professionals.")
    observation_results = models.TextField(
        help_text="Summarize the results of classroom observations, including the student's behavior, interaction with peers, and learning patterns.")


class LearningProfile(models.Model):
    CONDITION_STATUS = [
        ('NA', 'Not Applicable'),
        ('S', 'Suspected'),
        ('D', 'Diagnosed'),
    ]

    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='learning_profile')
    learning_disabilities = models.CharField(max_length=2, choices=CONDITION_STATUS, default='NA',
                                             help_text="Indicate the status of specific learning disabilities.")
    gifts_and_talents = models.CharField(max_length=2, choices=CONDITION_STATUS, default='NA',
                                         help_text="Note the status of exceptional abilities or talents.")
    multiple_disabilities = models.CharField(max_length=2, choices=CONDITION_STATUS, default='NA',
                                             help_text="Indicate the status of multiple disabilities.")
    physical_impairments = models.CharField(max_length=2, choices=CONDITION_STATUS, default='NA',
                                            help_text="Note the status of physical impairments.")
    hearing_impairments = models.CharField(max_length=2, choices=CONDITION_STATUS, default='NA',
                                           help_text="Indicate the status of hearing impairments.")
    visual_impairments = models.CharField(max_length=2, choices=CONDITION_STATUS, default='NA',
                                          help_text="Note the status of visual impairments.")
    intellectual_impairment = models.CharField(max_length=2, choices=CONDITION_STATUS, default='NA',
                                               help_text="Indicate the status of intellectual impairment.")
    autism_spectrum_disorder = models.CharField(max_length=2, choices=CONDITION_STATUS, default='NA',
                                                help_text="Note the status of autism spectrum disorder.")
    down_syndrome = models.CharField(max_length=2, choices=CONDITION_STATUS, default='NA',
                                     help_text="Indicate the status of Down syndrome.")
    global_development_delay = models.CharField(max_length=2, choices=CONDITION_STATUS, default='NA',
                                                help_text="Note the status of global development delay.")
    others = models.TextField(blank=True,
                              help_text="Specify any other relevant conditions or learning characteristics not covered by the above categories.")


class DevelopmentalArea(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='developmental_area')
    cognitive = models.BooleanField(default=False,
                                    help_text="Indicate if cognitive development (e.g., problem-solving, memory, attention) is a focus area for this student.")
    social_emotional = models.BooleanField(default=False,
                                           help_text="Check if social-emotional development (e.g., self-regulation, interpersonal skills) is a priority for this student.")
    physical = models.BooleanField(default=False,
                                   help_text="Note if physical development (e.g., fine motor skills, gross motor skills) is an area of focus.")
    language = models.BooleanField(default=False,
                                   help_text="Indicate if language development is a key area for improvement or support.")
    speaking = models.TextField(
        help_text="Describe the student's speaking abilities, including articulation, fluency, and expressive language skills.")
    reading = models.TextField(
        help_text="Detail the student's reading abilities, including decoding skills, fluency, and comprehension levels.")
    writing = models.TextField(
        help_text="Describe the student's writing abilities, including handwriting, spelling, and written expression skills.")
    listening = models.TextField(
        help_text="Detail the student's listening abilities, including attention span and auditory processing skills.")
    comprehension = models.TextField(
        help_text="Describe the student's comprehension abilities across various subjects and types of information.")
    others = models.TextField(blank=True,
                              help_text="Specify any other developmental areas or skills that require attention or support.")


class SkillsStrengths(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='skills_strengths')
    english = models.TextField(help_text="Describe the student's English skills.")
    dhivehi = models.TextField(help_text="Describe the student's Dhivehi skills.")
    math = models.TextField(help_text="Describe the student's Math skills.")
    quran_arabic = models.TextField(help_text="Describe the student's Quran/Arabic skills.")
    islam = models.TextField(help_text="Describe the student's Islam skills.")
    key_competencies = models.TextField(help_text="Describe the student's key competencies.")
    social_skills = models.TextField(help_text="Describe the student's social skills.")
    adaptive_behavior = models.TextField(help_text="Describe the student's adaptive behavior.")
    language_communication = models.TextField(help_text="Describe the student's language and communication skills.")
    others = models.TextField(blank=True, help_text="Specify any other relevant information.")


class AccessibleLearningSupport(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='accessible_learning_support')
    learning_environment = models.TextField(help_text="Describe the learning environment.")
    learning_materials = models.TextField(help_text="Describe the learning materials used.")
    adult_support = models.TextField(help_text="Describe the adult support available.")
    content = models.TextField(help_text="Describe the content of the learning materials.")
    methodology = models.TextField(help_text="Describe the methodology used in teaching.")
    assessment_modification = models.TextField(help_text="Describe any modifications to assessments.")


class Goal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='goals')
    area = models.CharField(max_length=255, help_text="Specify the area of focus for the goal.")
    annual_goal = models.TextField(help_text="Describe the annual goal for the student.")
    assessment_criteria = models.TextField(help_text="Describe the criteria for assessing the goal.")
    procedures = models.TextField(help_text="Describe the procedures for assessing the goal.")
    assessment_schedule = models.CharField(max_length=255, help_text="Specify the schedule for assessments.")
    responsible_person = models.CharField(max_length=255, help_text="Specify the person responsible for the goal.")


class InterventionService(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='intervention_services')
    program = models.CharField(max_length=255, help_text="Describe the intervention program.")
    frequency = models.CharField(max_length=100, help_text="Specify the frequency of the intervention.")
    duration = models.CharField(max_length=100, help_text="Specify the duration of the intervention.")
    location = models.CharField(max_length=255, help_text="Specify the location of the intervention.")
    initiation_date = models.DateField(help_text="Select the initiation date of the intervention.")


class SupplementaryService(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='supplementary_services')
    type_of_support = models.CharField(max_length=255, help_text="Describe the type of support provided.")
    time = models.CharField(max_length=100, help_text="Specify the time allocated for the support.")
    duration = models.CharField(max_length=100, help_text="Specify the duration of the support.")


class ICPParticipant(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='icp_participants')
    name = models.CharField(max_length=255, help_text="Enter the name of the participant.")
    designation = models.CharField(max_length=255, help_text="Enter the designation of the participant.")
    signature = models.TextField(help_text="Provide the signature of the participant.")
    date = models.DateField(help_text="Select the date of the participant's signature.")


class ImportantDates(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='important_dates')
    initial_referral = models.DateField(help_text="Select the date of the initial referral.")
    icp_meeting = models.DateField(help_text="Select the date of the ICP meeting.")
    implementation = models.DateField(help_text="Select the date of implementation.")
    review = models.DateField(help_text="Select the date for review.")


class TransitionPlan(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='transition_plan')
    current_stage = models.CharField(max_length=100, help_text="Enter the current educational stage.")
    next_stage = models.CharField(max_length=100, help_text="Enter the next educational stage.")
    transition_goals = models.TextField(help_text="Describe the goals for the transition.")
    support_needed = models.TextField(help_text="Describe the support needed for the transition.")
    responsible_persons = models.TextField(help_text="List the persons responsible for the transition.")


class Review(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reviews')
    review_date = models.DateField(help_text="Select the date of the review.")
    progress_summary = models.TextField(help_text="Summarize the progress since the last review.")
    goals_achieved = models.TextField(help_text="List the goals that have been achieved.")
    goals_in_progress = models.TextField(help_text="List the goals that are still in progress.")
    new_goals = models.TextField(help_text="List any new goals set during this review.")
    next_review_date = models.DateField(help_text="Select the date for the next review.")


class Document(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255, help_text="Enter the title of the document.")
    file = models.FileField(upload_to='student_documents/', help_text="Upload the document file.")
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, help_text="Provide a description of the document.")


class ICPTeam(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='icp_team')
    team_members = models.ManyToManyField(User, related_name='icp_teams')
    formation_date = models.DateField(help_text="Select the date when the ICP team was formed.")


class ReferralSystem(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='referrals')
    referring_teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals_made')
    referral_date = models.DateField(help_text="Select the date of the referral.")
    reason_for_referral = models.TextField(help_text="Describe the reason for the referral.")
    status = models.CharField(max_length=50,
                              choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])
    approval_date = models.DateField(null=True, blank=True, help_text="Select the date of approval or rejection.")
    approver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='referrals_approved')
