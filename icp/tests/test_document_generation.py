from django.test import TestCase, Client
from django.urls import reverse
from icp.models import Student, GeneralInformation
from django.core.files.uploadedfile import SimpleUploadedFile

class TestDocumentGeneration(TestCase):
    def setUp(self):
        self.client = Client()
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

    def test_generate_icp(self):
        response = self.client.get(reverse('generate_icp', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        self.assertEqual(response['Content-Disposition'], f'attachment; filename={self.student.name}_ICP.docx')

    def test_goal_added_view(self):
        response = self.client.get(reverse('goal_added', kwargs={'student_id': self.student.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'icp/goal_added.html')
