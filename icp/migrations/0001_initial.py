# Generated by Django 5.1 on 2024-09-11 20:11

import django.db.models.deletion
import icp.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the student's full name as it appears on official documents.", max_length=255)),
                ('id_card_number', models.CharField(help_text="Enter the student's ID card number for official identification.", max_length=7, validators=[icp.models.validate_id_card_number])),
                ('ie_program', models.CharField(choices=[('mainstream', 'Mainstream Program'), ('school_readiness', 'School Readiness'), ('early_intervention', 'Early Intervention'), ('homeschooling', 'Homeschooling')], help_text='Specify the Inclusive Education (IE) program the student is enrolled in.', max_length=255)),
                ('date_of_document', models.DateField(help_text='Select the date when this ICP document is being created or last updated.')),
                ('current_education_level', models.CharField(help_text="Indicate the student's current grade level or educational stage.", max_length=100)),
                ('academic_strengths', models.TextField(help_text="Describe the student's academic strengths, including subjects or skills where they excel.")),
                ('areas_of_interest', models.TextField(help_text="List the student's areas of interest, both academic and non-academic, to help tailor their learning experience.")),
            ],
        ),
        migrations.CreateModel(
            name='SkillsStrengths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.TextField(help_text="Describe the student's English skills.")),
                ('dhivehi', models.TextField(help_text="Describe the student's Dhivehi skills.")),
                ('math', models.TextField(help_text="Describe the student's Math skills.")),
                ('quran_arabic', models.TextField(help_text="Describe the student's Quran/Arabic skills.")),
                ('islam', models.TextField(help_text="Describe the student's Islam skills.")),
                ('key_competencies', models.TextField(help_text="Describe the student's key competencies.")),
                ('social_skills', models.TextField(help_text="Describe the student's social skills.")),
                ('adaptive_behavior', models.TextField(help_text="Describe the student's adaptive behavior.")),
                ('language_communication', models.TextField(help_text="Describe the student's language and communication skills.")),
                ('others', models.TextField(blank=True, help_text='Specify any other relevant information.')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='skills_strengths', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateField(help_text='Select the date of the review.')),
                ('progress_summary', models.TextField(help_text='Summarize the progress since the last review.')),
                ('goals_achieved', models.TextField(help_text='List the goals that have been achieved.')),
                ('goals_in_progress', models.TextField(help_text='List the goals that are still in progress.')),
                ('new_goals', models.TextField(help_text='List any new goals set during this review.')),
                ('next_review_date', models.DateField(help_text='Select the date for the next review.')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='ReferralSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_date', models.DateField(help_text='Select the date of the referral.')),
                ('reason_for_referral', models.TextField(help_text='Describe the reason for the referral.')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=50)),
                ('approval_date', models.DateField(blank=True, help_text='Select the date of approval or rejection.', null=True)),
                ('approver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referrals_approved', to=settings.AUTH_USER_MODEL)),
                ('referring_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals_made', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='LearningProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning_disabilities', models.CharField(choices=[('NA', 'Not Applicable'), ('S', 'Suspected'), ('D', 'Diagnosed')], default='NA', help_text='Indicate the status of specific learning disabilities.', max_length=2)),
                ('gifts_and_talents', models.CharField(choices=[('NA', 'Not Applicable'), ('S', 'Suspected'), ('D', 'Diagnosed')], default='NA', help_text='Note the status of exceptional abilities or talents.', max_length=2)),
                ('multiple_disabilities', models.CharField(choices=[('NA', 'Not Applicable'), ('S', 'Suspected'), ('D', 'Diagnosed')], default='NA', help_text='Indicate the status of multiple disabilities.', max_length=2)),
                ('physical_impairments', models.CharField(choices=[('NA', 'Not Applicable'), ('S', 'Suspected'), ('D', 'Diagnosed')], default='NA', help_text='Note the status of physical impairments.', max_length=2)),
                ('hearing_impairments', models.CharField(choices=[('NA', 'Not Applicable'), ('S', 'Suspected'), ('D', 'Diagnosed')], default='NA', help_text='Indicate the status of hearing impairments.', max_length=2)),
                ('visual_impairments', models.CharField(choices=[('NA', 'Not Applicable'), ('S', 'Suspected'), ('D', 'Diagnosed')], default='NA', help_text='Note the status of visual impairments.', max_length=2)),
                ('intellectual_impairment', models.CharField(choices=[('NA', 'Not Applicable'), ('S', 'Suspected'), ('D', 'Diagnosed')], default='NA', help_text='Indicate the status of intellectual impairment.', max_length=2)),
                ('autism_spectrum_disorder', models.CharField(choices=[('NA', 'Not Applicable'), ('S', 'Suspected'), ('D', 'Diagnosed')], default='NA', help_text='Note the status of autism spectrum disorder.', max_length=2)),
                ('down_syndrome', models.CharField(choices=[('NA', 'Not Applicable'), ('S', 'Suspected'), ('D', 'Diagnosed')], default='NA', help_text='Indicate the status of Down syndrome.', max_length=2)),
                ('global_development_delay', models.CharField(choices=[('NA', 'Not Applicable'), ('S', 'Suspected'), ('D', 'Diagnosed')], default='NA', help_text='Note the status of global development delay.', max_length=2)),
                ('others', models.TextField(blank=True, help_text='Specify any other relevant conditions or learning characteristics not covered by the above categories.')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='learning_profile', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='InterventionService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(help_text='Describe the intervention program.', max_length=255)),
                ('frequency', models.CharField(help_text='Specify the frequency of the intervention.', max_length=100)),
                ('duration', models.CharField(help_text='Specify the duration of the intervention.', max_length=100)),
                ('location', models.CharField(help_text='Specify the location of the intervention.', max_length=255)),
                ('initiation_date', models.DateField(help_text='Select the initiation date of the intervention.')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intervention_services', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='ImportantDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_referral', models.DateField(help_text='Select the date of the initial referral.')),
                ('icp_meeting', models.DateField(help_text='Select the date of the ICP meeting.')),
                ('implementation', models.DateField(help_text='Select the date of implementation.')),
                ('review', models.DateField(help_text='Select the date for review.')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='important_dates', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='ICPTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation_date', models.DateField(help_text='Select the date when the ICP team was formed.')),
                ('team_members', models.ManyToManyField(related_name='icp_teams', to=settings.AUTH_USER_MODEL)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='icp_team', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='ICPParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the participant.', max_length=255)),
                ('designation', models.CharField(help_text='Enter the designation of the participant.', max_length=255)),
                ('signature', models.TextField(help_text='Provide the signature of the participant.')),
                ('date', models.DateField(help_text="Select the date of the participant's signature.")),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icp_participants', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(help_text='Specify the area of focus for the goal.', max_length=255)),
                ('annual_goal', models.TextField(help_text='Describe the annual goal for the student.')),
                ('assessment_criteria', models.TextField(help_text='Describe the criteria for assessing the goal.')),
                ('procedures', models.TextField(help_text='Describe the procedures for assessing the goal.')),
                ('assessment_schedule', models.CharField(help_text='Specify the schedule for assessments.', max_length=255)),
                ('responsible_person', models.CharField(help_text='Specify the person responsible for the goal.', max_length=255)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_concerns', models.TextField(help_text="Document any concerns expressed by the parents regarding the student's education or development.")),
                ('medical_alerts', models.TextField(help_text="List any medical conditions, allergies, or health-related issues that may affect the student's learning or require attention during school hours.")),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='general_information', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of the document.', max_length=255)),
                ('file', models.FileField(help_text='Upload the document file.', upload_to='student_documents/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, help_text='Provide a description of the document.')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='DevelopmentalArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cognitive', models.BooleanField(default=False, help_text='Indicate if cognitive development (e.g., problem-solving, memory, attention) is a focus area for this student.')),
                ('social_emotional', models.BooleanField(default=False, help_text='Check if social-emotional development (e.g., self-regulation, interpersonal skills) is a priority for this student.')),
                ('physical', models.BooleanField(default=False, help_text='Note if physical development (e.g., fine motor skills, gross motor skills) is an area of focus.')),
                ('language', models.BooleanField(default=False, help_text='Indicate if language development is a key area for improvement or support.')),
                ('speaking', models.TextField(help_text="Describe the student's speaking abilities, including articulation, fluency, and expressive language skills.")),
                ('reading', models.TextField(help_text="Detail the student's reading abilities, including decoding skills, fluency, and comprehension levels.")),
                ('writing', models.TextField(help_text="Describe the student's writing abilities, including handwriting, spelling, and written expression skills.")),
                ('listening', models.TextField(help_text="Detail the student's listening abilities, including attention span and auditory processing skills.")),
                ('comprehension', models.TextField(help_text="Describe the student's comprehension abilities across various subjects and types of information.")),
                ('others', models.TextField(blank=True, help_text='Specify any other developmental areas or skills that require attention or support.')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='developmental_area', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='AccessibleLearningSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning_environment', models.TextField(help_text='Describe the learning environment.')),
                ('learning_materials', models.TextField(help_text='Describe the learning materials used.')),
                ('adult_support', models.TextField(help_text='Describe the adult support available.')),
                ('content', models.TextField(help_text='Describe the content of the learning materials.')),
                ('methodology', models.TextField(help_text='Describe the methodology used in teaching.')),
                ('assessment_modification', models.TextField(help_text='Describe any modifications to assessments.')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accessible_learning_support', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentEvaluationSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosed_conditions', models.TextField(help_text="List any officially diagnosed conditions that impact the student's learning, as documented by qualified professionals.")),
                ('observation_results', models.TextField(help_text="Summarize the results of classroom observations, including the student's behavior, interaction with peers, and learning patterns.")),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_summary', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='SupplementaryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_support', models.CharField(help_text='Describe the type of support provided.', max_length=255)),
                ('time', models.CharField(help_text='Specify the time allocated for the support.', max_length=100)),
                ('duration', models.CharField(help_text='Specify the duration of the support.', max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplementary_services', to='icp.student')),
            ],
        ),
        migrations.CreateModel(
            name='TransitionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_stage', models.CharField(help_text='Enter the current educational stage.', max_length=100)),
                ('next_stage', models.CharField(help_text='Enter the next educational stage.', max_length=100)),
                ('transition_goals', models.TextField(help_text='Describe the goals for the transition.')),
                ('support_needed', models.TextField(help_text='Describe the support needed for the transition.')),
                ('responsible_persons', models.TextField(help_text='List the persons responsible for the transition.')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transition_plan', to='icp.student')),
            ],
        ),
    ]
