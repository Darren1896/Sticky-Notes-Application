from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Note instances.

    This form is based on the Note model and includes fields for the title
    and content of the note. The created_at field is excluded as it is
    automatically set when a note is created.
    """

    class Meta:
        model = Note
        fields = ['title', 'content',]
