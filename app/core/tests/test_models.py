from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email="test@test.com"
        password="testpass123"
        user_model=get_user_model()
        user=user_model.objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        """Test The email for new user is normalized or not """

        email="test@TEST.COM"
        user=get_user_model().objects.create_user(email,'test1234')

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test Creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_new_superuser(self):
        """"Test Creating New Super User"""
        user=get_user_model().objects.create_superuser(
            'test@test.com', 
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)