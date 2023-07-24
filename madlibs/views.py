from django.shortcuts import render, redirect

from .models import Story, Processed
from .utils import extract_words, convert_text, interpolate
# from .forms import StoryForm


def stories(request):
    story_list = Story.objects.all()
    context = {
        'story_list': story_list
    }
    return render(request, 'stories.html', context)


def index(request):
    return render(request, 'index.html')


def story(request, story_id):
    item = Story.objects.get(pk=story_id)
    word_list = extract_words(item.story_text)
    context = {
        'story': item,
        'story_words': word_list,
    }

    if (request.method == 'POST'):
        # 1. get words and story text
        story_text = convert_text(item.story_text)
        # form = StoryForm(3)
        print(request.POST)
        story_words = []
        # 2. insert record into Processed table
        record = Processed(story_text=story_text, story_words=story_words, story_id=story_id)
        record.save()
        # 3. display
        return redirect('madlibs:read_story', record_id=record.id)


    return render(request, 'play.html', context)


def read_story(request, record_id):
    record = Processed.objects.get(pk=record_id)
    record_story = Story.objects.get(pk=record.story_id)
    story_text = interpolate(record)

    context = {
        'record_story': record_story,
        'story_text': story_text,
    }
    return render(request, 'read_story.html', context)

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')