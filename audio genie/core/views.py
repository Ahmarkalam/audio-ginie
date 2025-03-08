from django.shortcuts import render

# Create your views here.

import openai
from django.shortcuts import render, redirect
from .models import AudioFile
from .forms import AudioFileForm
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def home(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AudioFileForm()

    audio_files = AudioFile.objects.all()
    return render(request, 'core/home.html', {'form': form, 'audio_files': audio_files})

def summarize_audio(request, audio_id):
    audio_file = AudioFile.objects.get(id=audio_id)
    audio_path = audio_file.audio.path

    try:
        with open(audio_path, 'rb') as audio:
            transcript = openai.Audio.transcribe("whisper-1", audio)
            summary = transcript['text']
    except Exception as e:
        summary = f"Error: {e}"

    return render(request, 'core/summarize.html', {'audio_file': audio_file, 'summary': summary})

