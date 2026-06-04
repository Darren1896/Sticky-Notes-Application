from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    View to display a list of all sticky notes.

    Retrieves all Note objects from the database and renders them in the
    'note_list.html' template.
    """
    notes = Note.objects.all()

    context = {
        'notes': notes,
    }
    return render(request, 'notes/note_list.html', context)


def note_detail(request, pk):
    """
    View to display the details of a specific sticky note.

    Retrieves a Note object based on the provided primary key (pk) and renders
    it in the 'note_detail.html' template.
    If the Note does not exist, a 404 error is raised.
    """
    note = get_object_or_404(Note, pk=pk)

    return render(request, 'notes/note_detail.html', {"note": note})


def note_create(request):
    """
    View to create a new sticky note.

    Handles both GET and POST requests. On GET, it renders an empty NoteForm
    in the 'note_form.html' template.
    On POST, it validates the submitted form data and creates a new Note
    object if the data is valid.
    After successful creation, it redirects to the note list view.
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'notes/note_form.html', {'form': form})


def note_update(request, pk):
    """
    View to update an existing sticky note.

    Handles both GET and POST requests. On GET, it retrieves the Note object
    based on the provided primary key (pk)
    and renders a NoteForm pre-filled with the note's data in the
    'note_form.html' template.
    On POST, it validates the submitted form data and updates the Note object
    if the data is valid.
    After successful update, it redirects to the note detail view.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    """
    View to delete an existing sticky note.

    Handles POST requests. It retrieves the Note object based on the provided
    primary key (pk) and deletes it from the database.
    After successful deletion, it redirects to the note list view.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
