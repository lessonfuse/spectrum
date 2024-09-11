from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from icp.models import Student, GeneralInformation, LearningProfile, DevelopmentalArea, SkillsStrengths, AccessibleLearningSupport, Goal, InterventionService, SupplementaryService
from django.core.files.uploadedfile import SimpleUploadedFile

class TestDocumentGeneration(TestCase):
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
        GeneralInformation.objects.create(
            student=self.student,
            parent_concerns="Test concerns",
            medical_alerts="Test alerts"
        )
        LearningProfile.objects.create(
            student=self.student,
            learning_disabilities="S",
            gifts_and_talents="NA"
        )
        DevelopmentalArea.objects.create(
            student=self.student,
            cognitive=True,
            social_emotional=False
        )
        SkillsStrengths.objects.create(
            student=self.student,
            english="Good",
            math="Excellent"
        )
        AccessibleLearningSupport.objects.create(
            student=self.student,
            learning_environment="Quiet classroom",
            learning_materials="Visual aids"
        )
        Goal.objects.create(
            student=self.student,
            area="Math",
            annual_goal="Improve problem-solving skills"
        )
        InterventionService.objects.create(
            student=self.student,
            program="Math tutoring",
            frequency="Twice a week"
        )
        SupplementaryService.objects.create(
            student=self.student,
            type_of_support="Speech therapy",
            time="Once a week"
        )

    def test_generate_icp(self):
        response = self.client.get(reverse('generate_icp', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        self.assertEqual(response['Content-Disposition'], f'attachment; filename={self.student.name}_ICP.docx')

        # Check if the generated document contains expected content
        content = response.content.decode('latin-1')
        self.assertIn("Test Student", content)
        self.assertIn("A123456", content)
        self.assertIn("Test concerns", content)
        self.assertIn("Test alerts", content)
        self.assertIn("Math tutoring", content)
        self.assertIn("Speech therapy", content)

    def test_goal_added_view(self):
        response = self.client.get(reverse('goal_added', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'icp/goal_added.html')
        self.assertContains(response, "Goal has been added successfully")

    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.get(reverse('generate_icp', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={reverse("generate_icp", kwargs={"student_id": self.student.id})}')
