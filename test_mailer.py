from fastapi.testclient import TestClient
from unittest.mock import patch
import unittest
from main import app

client = TestClient(app)


class TestEmail(unittest.TestCase):

    @patch('main.send_email', return_value=True)
    @patch.dict('os.environ', {'SMTP_EMAIL': 'test_email', 'SMTP_PASSWORD': 'test_password'})
    def test_send_email_successful(self, mock_send_email):
        response = client.post(
            "/send_email/",
            json={
                "to": "test@example.com",
                "subject": "Test Subject",
                "message": "Test Message"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "email sent"})
        mock_send_email.assert_called_once()

    @patch('main.send_email', return_value=False)
    @patch.dict('os.environ', {'SMTP_EMAIL': 'test_email', 'SMTP_PASSWORD': 'test_password'})
    def test_send_email_failure(self, mock_send_email):
        response = client.post(
            "/send_email/",
            json={
                "to": "test@example.com",
                "subject": "Test Subject",
                "message": "Test Message"
            }
        )
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"detail": "Failed to send email"})
        mock_send_email.assert_called_once()

    @patch.dict('os.environ', {'SMTP_EMAIL': '', 'SMTP_PASSWORD': ''})
    def test_no_smtp_credentials(self):
        response = client.post(
            "/send_email/",
            json={
                "to": "test@example.com",
                "subject": "Test Subject",
                "message": "Test Message"
            }
        )
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json(), {"detail": "SMTP credentials are not set"})


if __name__ == '__main__':
    unittest.main()
