from django.test import TestCase, Client
from django.urls import reverse, NoReverseMatch
from icp.models import Student
from django.contrib.auth.models import User

class TestStudentCRUDViews(TestCase):
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

    def test_student_create_view(self):
        response = self.client.get(reverse('create_icp'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/create.html')

        data = {
            'name': 'New Student',
            'id_card_number': 'A654321',
            'ie_program': 'mainstream',
            'date_of_document': '2023-06-01',
            'current_education_level': 'Grade 6'
        }
        response = self.client.post(reverse('create_icp'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Student.objects.filter(name='New Student').exists())
        new_student = Student.objects.get(name='New Student')
        self.assertRedirects(response, reverse('general_information', kwargs={'student_id': new_student.id}))

    def test_student_update_view(self):
        response = self.client.get(reverse('student_update', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/update.html')

        data = {
            'name': 'Updated Student',
            'id_card_number': 'A123456',
            'ie_program': 'school_readiness',
            'date_of_document': '2023-06-01',
            'current_education_level': 'Grade 5'
        }
        response = self.client.post(reverse('student_update', kwargs={'pk': self.student.pk}), data)
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, 'Updated Student')
        self.assertEqual(self.student.ie_program, 'school_readiness')
        self.assertRedirects(response, reverse('student_detail', kwargs={'pk': self.student.pk}))

    def test_student_delete_view(self):
        response = self.client.get(reverse('student_delete', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/delete.html')

        response = self.client.post(reverse('student_delete', kwargs={'pk': self.student.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())
        self.assertRedirects(response, reverse('list_icps'))

        # Check if the template is using the correct URL
        with self.assertRaises(NoReverseMatch):
            reverse('asset_detail')

    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.get(reverse('create_icp'))
        self.assertEqual(response.status_code, 200)
