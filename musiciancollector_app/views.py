from django.shortcuts import render
# from django.http import HttpResponse

musicians = [
    {"name": "John Lennon", "instrument": "Guitar", "genre": "Rock", "band": "The Beatles"},
    {"name": "Miles Davis", "instrument": "Trumpet", "genre": "Jazz", "solo_artist": True},
    {"name": "Taylor Swift", "instrument": "Guitar", "genre": "Pop", "solo_artist": True},
    {"name": "Freddie Mercury", "instrument": "Piano", "genre": "Rock", "band": "Queen"},
    {"name": "Beyoncé", "instrument": "Vocals", "genre": "R&B", "solo_artist": True},
    {"name": "Yo-Yo Ma", "instrument": "Cello", "genre": "Classical", "solo_artist": True},
    {"name": "Kurt Cobain", "instrument": "Guitar", "genre": "Grunge", "band": "Nirvana"},
    {"name": "Duke Ellington", "instrument": "Piano", "genre": "Jazz", "band": "Duke Ellington Orchestra"}
]

# Create your views here.
def home(request):
    return render(request, 'musicians/home.html')

def about(request):
    return render(request, 'musicians/about.html')

def musicians_index(request):
    return render(request, 'musicians/index.html', {
        'musicians': musicians
    })