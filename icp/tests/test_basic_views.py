from django.test import TestCase, Client
from django.urls import reverse
from icp.models import Student

class TestBasicViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.student = Student.objects.create(
            name="Test Student",
            id_card_number="A123456",
            ie_program="mainstream",
            date_of_document="2023-01-01",
            current_education_level="Grade 5"
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'icp/home.html')

    def test_icp_list_view(self):
        response = self.client.get(reverse('list_icps'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'icp/list.html')
        self.assertIn('students', response.context)

    def test_student_detail_view(self):
        response = self.client.get(reverse('student_detail', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'icp/student_detail.html')
        self.assertEqual(response.context['student'], self.student)

    def test_icp_success_view(self):
        response = self.client.get(reverse('icp_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'icp/success.html')
