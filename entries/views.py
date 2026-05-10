from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Entry
from .forms import EntryForm

@login_required
def entry_list(request):
    query = request.GET.get('q', '')
    entries = Entry.objects.filter(author=request.user)

    if query:
        entries = entries.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    return render(request, 'entries/entry_list.html', {
        'entries': entries,
        'query': query
    })

@login_required
def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    return render(request, 'entries/entry_detail.html', {'entry': entry})

@login_required
def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = EntryForm()
    return render(request, 'entries/entry_form.html', {'form': form, 'action': 'Создать'})

@login_required
def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'entries/entry_form.html', {
        'form': form,
        'action': 'Редактировать',
        'entry': entry
    })

@login_required
def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk, author=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'entries/entry_confirm_delete.html', {'entry': entry})