from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from icp.models import Student, GeneralInformation, LearningProfile, DevelopmentalArea, SkillsStrengths, AccessibleLearningSupport, Goal, InterventionService, SupplementaryService

class TestICPSectionViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.student = Student.objects.create(
            name="Test Student",
            id_card_number="A123456",
            ie_program="mainstream",
            date_of_document="2023-01-01",
            current_education_level="Grade 5"
        )

    def test_general_information_view(self):
        response = self.client.get(reverse('general_information', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/create.html')

        data = {
            'parent_concerns': 'Test concerns',
            'medical_alerts': 'Test alerts'
        }
        response = self.client.post(reverse('general_information', kwargs={'student_id': self.student.id}), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(GeneralInformation.objects.filter(student=self.student).exists())
        self.assertRedirects(response, reverse('learning_profile', kwargs={'student_id': self.student.id}))

    def test_learning_profile_view(self):
        response = self.client.get(reverse('learning_profile', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/create.html')

        data = {
            'learning_disabilities': 'S',
            'gifts_and_talents': 'NA',
            'multiple_disabilities': 'NA',
            'physical_impairments': 'NA',
            'hearing_impairments': 'NA',
            'visual_impairments': 'NA',
            'intellectual_impairment': 'NA',
            'autism_spectrum_disorder': 'NA',
            'down_syndrome': 'NA',
            'global_development_delay': 'NA',
            'others': 'Test others'
        }
        response = self.client.post(reverse('learning_profile', kwargs={'student_id': self.student.id}), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(LearningProfile.objects.filter(student=self.student).exists())
        self.assertRedirects(response, reverse('developmental_areas', kwargs={'student_id': self.student.id}))

    def test_developmental_areas_view(self):
        response = self.client.get(reverse('developmental_areas', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/create.html')

        data = {
            'cognitive': True,
            'social_emotional': False,
            'physical': True,
            'language': False,
            'speaking': 'Test speaking',
            'reading': 'Test reading',
            'writing': 'Test writing',
            'listening': 'Test listening',
            'comprehension': 'Test comprehension',
            'others': 'Test others'
        }
        response = self.client.post(reverse('developmental_areas', kwargs={'student_id': self.student.id}), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(DevelopmentalArea.objects.filter(student=self.student).exists())
        self.assertRedirects(response, reverse('skills_strengths', kwargs={'student_id': self.student.id}))

    def test_skills_strengths_view(self):
        response = self.client.get(reverse('skills_strengths', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/create.html')

        data = {
            'english': 'Test English',
            'dhivehi': 'Test Dhivehi',
            'math': 'Test Math',
            'quran_arabic': 'Test Quran/Arabic',
            'islam': 'Test Islam',
            'key_competencies': 'Test competencies',
            'social_skills': 'Test social skills',
            'adaptive_behavior': 'Test adaptive behavior',
            'language_communication': 'Test language',
            'others': 'Test others'
        }
        response = self.client.post(reverse('skills_strengths', kwargs={'student_id': self.student.id}), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(SkillsStrengths.objects.filter(student=self.student).exists())
        self.assertRedirects(response, reverse('accessible_learning_support', kwargs={'student_id': self.student.id}))

    def test_accessible_learning_support_view(self):
        response = self.client.get(reverse('accessible_learning_support', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/create.html')

        data = {
            'learning_environment': 'Test environment',
            'learning_materials': 'Test materials',
            'adult_support': 'Test support',
            'content': 'Test content',
            'methodology': 'Test methodology',
            'assessment_modification': 'Test modification'
        }
        response = self.client.post(reverse('accessible_learning_support', kwargs={'student_id': self.student.id}), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(AccessibleLearningSupport.objects.filter(student=self.student).exists())
        self.assertRedirects(response, reverse('measurable_goals', kwargs={'student_id': self.student.id}))

    def test_measurable_goals_view(self):
        response = self.client.get(reverse('measurable_goals', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/create.html')

        data = {
            'area': 'Test area',
            'annual_goal': 'Test goal',
            'assessment_criteria': 'Test criteria',
            'procedures': 'Test procedures',
            'assessment_schedule': 'Test schedule',
            'responsible_person': 'Test person'
        }
        response = self.client.post(reverse('measurable_goals', kwargs={'student_id': self.student.id}), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Goal.objects.filter(student=self.student).exists())
        self.assertRedirects(response, reverse('goal_added', kwargs={'student_id': self.student.id}))

    def test_intervention_services_view(self):
        response = self.client.get(reverse('intervention_services', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/create.html')

        data = {
            'program': 'Test program',
            'frequency': 'Test frequency',
            'duration': 'Test duration',
            'location': 'Test location',
            'initiation_date': '2023-06-01'
        }
        response = self.client.post(reverse('intervention_services', kwargs={'student_id': self.student.id}), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(InterventionService.objects.filter(student=self.student).exists())
        self.assertRedirects(response, reverse('supplementary_services', kwargs={'student_id': self.student.id}))

    def test_supplementary_services_view(self):
        response = self.client.get(reverse('supplementary_services', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/create.html')

        data = {
            'type_of_support': 'Test support',
            'time': 'Test time',
            'duration': 'Test duration'
        }
        response = self.client.post(reverse('supplementary_services', kwargs={'student_id': self.student.id}), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(SupplementaryService.objects.filter(student=self.student).exists())
        self.assertRedirects(response, reverse('generate_icp', kwargs={'student_id': self.student.id}))

    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.get(reverse('general_information', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={reverse("general_information", kwargs={"student_id": self.student.id})}')
