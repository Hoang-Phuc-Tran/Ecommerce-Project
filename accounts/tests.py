from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.contrib.auth import get_user_model
from .models import Account, UserProfile

User = get_user_model()

class AccountTests(TestCase):
    def setUp(self):
        # Setup data for all tests
        self.user = User.objects.create_user(
            first_name='Test',
            last_name='User',
            username='testuser',
            email='testuser@example.com',
            password='testpassword123',
        )
        self.user.is_active = True
        self.user.save()
        UserProfile.objects.create(
            user=self.user,
            profile_picture='default/default-user.png',
            address_line_1='123 Test St',
            city='Testville',
            state='TS',
            country='Testland'
        )


    def test_register_user(self):
        # Test the registration functionality
        response = self.client.post(reverse('register'), data={
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'email': 'johndoe@example.com',
            'password': 's3cr3tpassword',
            'confirm_password': 's3cr3tpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='johndoe@example.com').exists())
        self.assertEqual(len(mail.outbox), 1)  # Check that an email has been sent

    def test_login_user(self):
        # Test the login functionality
        response = self.client.post(reverse('login'), data={
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        })
        self.assertRedirects(response, reverse('dashboard'))

    def test_logout_user(self):
        # Test the logout functionality
        self.client.login(email='testuser@example.com', password='testpassword123')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))

    def test_forgot_password(self):
        # Test the forgot password functionality
        response = self.client.post(reverse('forgotPassword'), {'email': 'testuser@example.com'})
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(len(mail.outbox), 1)  # Check that an email has been sent





