from django.db import models


class Note(models.Model):
    """
    Model representing a sticky note.

    Fields:
    - title: The title of the note.
    - content: The content of the note.
    - created_at: The timestamp when the note was created.

    Methods:
    - __str__: Returns the title of the note for easy identification.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
