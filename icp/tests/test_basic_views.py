from django.test import TestCase, Client
from django.urls import reverse
from icp.models import Student
from django.contrib.auth.models import User

class TestBasicViews(TestCase):
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

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'icp/home.html')

    def test_icp_list_view(self):
        response = self.client.get(reverse('list_icps'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'icp/list.html')
        self.assertIn('students', response.context)
        self.assertQuerysetEqual(response.context['students'], [repr(self.student)])

    def test_student_detail_view(self):
        response = self.client.get(reverse('student_detail', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'icp/student_detail.html')
        self.assertEqual(response.context['student'], self.student)

    def test_icp_success_view(self):
        response = self.client.get(reverse('icp_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'icp/success.html')

    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.get(reverse('list_icps'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={reverse("list_icps")}')
