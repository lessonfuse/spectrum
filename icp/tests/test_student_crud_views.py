from django.test import TestCase, Client
from django.urls import reverse
from icp.models import Student
from django.contrib.auth.models import User
from django.utils import timezone

class TestStudentCreateView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.url = reverse('student_create')

    def test_get_create_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic/create.html')
        self.assertContains(response, 'Create Student')

    def test_post_create_view_valid_data(self):
        data = {
            'name': 'John Doe',
            'id_card_number': '1234567890',
            'ie_program': 'Program A',
            'date_of_document': timezone.now().date().isoformat()
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertTrue(Student.objects.filter(name='John Doe').exists())

    def test_post_create_view_invalid_data(self):
        data = {
            'name': '',  # Invalid: empty name
            'id_card_number': '1234567890',
            'ie_program': 'Program A',
            'date_of_document': timezone.now().date().isoformat()
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)  # Stay on the same page
        self.assertFalse(Student.objects.filter(id_card_number='1234567890').exists())
        self.assertFormError(response, 'form', 'name', 'This field is required.')

    def test_redirect_after_creation(self):
        data = {
            'name': 'Jane Doe',
            'id_card_number': '0987654321',
            'ie_program': 'Program B',
            'date_of_document': timezone.now().date().isoformat()
        }
        response = self.client.post(self.url, data)
        new_student = Student.objects.get(name='Jane Doe')
        expected_url = reverse('general_information', kwargs={'student_id': new_student.id})
        self.assertRedirects(response, expected_url)

    def test_date_picker_widget(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'flatpickr')
        self.assertContains(response, 'minDate')

    def test_context_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['title'], 'Create Student')

    def test_form_class(self):
        response = self.client.get(self.url)
        form = response.context['form']
        self.assertIn('date_of_document', form.fields)
        self.assertEqual(form.fields['date_of_document'].widget.__class__.__name__, 'DatePickerInput')
