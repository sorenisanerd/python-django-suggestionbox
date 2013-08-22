from suggestionbox import models

from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('title', 'description')

def list_suggestions(request):
    if request.method == "POST":
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('suggestion_list'))
    else:
        form = SuggestionForm()

    return render(request, "list.html", 
                  {"suggestions": models.Comment.suggestions.all(),
                   "form": form })

def quotify(s):
    return '\n'.join([quotify_line(l) for l in s.split('\n')])

def quotify_line(l):
    prepend = '> '

    if l[:2] == '> ':
        prepend = '>'

    return '%s%s' % (prepend, l)

def suggestion_detail(request, top_id):
    suggestion = get_object_or_404(models.Comment, pk=top_id)

    if request.method == "POST":
        form = SuggestionForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.in_reply_to = suggestion
            comment.save()
            return HttpResponseRedirect(reverse('suggestion_detail',
                                                kwargs={"top_id": comment.id}))
    else:
        if suggestion.title[:3].lower() == 're:':
            title = suggestion.title
        else:
            title = 're: %s' % (suggestion.title,)
        form = SuggestionForm(initial={"title": title,
                                       "description": quotify(suggestion.description)})

    return render(request, "detail.html", 
                  {"suggestion": suggestion,
                   "form": form })


