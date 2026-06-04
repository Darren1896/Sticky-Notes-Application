from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, 'Test Note')
        self.assertEqual(self.note.content, 'This is a test note.')
        self.assertIsNotNone(self.note.created_at)

    def test_note_str_representation(self):
        self.assertEqual(str(self.note), 'Test Note')


class NoteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note.'
        )

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        response = self.client.get(reverse('note_detail', kwargs={'pk': self.note.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test note.')

    def test_note_create_view(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'This is a new note.'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Note.objects.filter(title='New Note').exists())

    def test_note_update_view(self):
        response = self.client.post(reverse('note_update', kwargs={'pk': self.note.pk}), {
            'title': 'Updated Note',
            'content': 'This is an updated note.'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after update
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')
        self.assertEqual(self.note.content, 'This is an updated note.')

    def test_note_delete_view(self):
        response = self.client.post(reverse('note_delete', kwargs={'pk': self.note.pk}))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
