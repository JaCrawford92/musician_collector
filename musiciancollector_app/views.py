from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Musician

# musicians = [
#     {"name": "John Lennon", "instrument": "Guitar", "genre": "Rock", "bio": "A key member of The Beatles, John Lennon was instrumental in the evolution of rock music.", "body_of_works": 11},  # Includes solo and The Beatles
#     {"name": "Miles Davis", "instrument": "Trumpet", "genre": "Jazz", "bio": "Miles Davis was an innovative jazz musician known for his influential contributions to the genre.", "body_of_works": 48},  # Studio albums
#     {"name": "Taylor Swift", "instrument": "Guitar", "genre": "Pop", "bio": "Taylor Swift is a singer-songwriter known for her narrative songwriting which often centers around her personal life.", "body_of_works": 10},  # Studio albums
#     {"name": "Freddie Mercury", "instrument": "Piano", "genre": "Rock", "bio": "The lead vocalist of Queen, Freddie Mercury was known for his flamboyant stage persona and powerful voice.", "body_of_works": 15},  # With Queen and solo
#     {"name": "Beyoncé", "instrument": "Vocals", "genre": "R&B", "bio": "Beyoncé is a global icon known for her powerful vocals and dynamic performances.", "body_of_works": 7},  # Studio albums
#     {"name": "Yo-Yo Ma", "instrument": "Cello", "genre": "Classical", "bio": "Yo-Yo Ma is a celebrated cellist known for his wide-ranging interests in different musical genres and cultures.", "body_of_works": 90},  # Includes collaborations and solo albums
#     {"name": "Kurt Cobain", "instrument": "Guitar", "genre": "Grunge", "bio": "As the frontman of Nirvana, Kurt Cobain brought grunge music to the forefront of the music scene in the early 90s.", "body_of_works": 3},  # Studio albums with Nirvana
#     {"name": "Duke Ellington", "instrument": "Piano", "genre": "Jazz", "bio": "Duke Ellington was a pivotal figure in the development of jazz and led his orchestra for more than fifty years.", "body_of_works": 70},  # Includes extensive discography with many albums
#     {"name": "Bob Marley", "instrument": "Guitar", "genre": "Reggae", "bio": "Bob Marley was a Jamaican singer-songwriter who became an international musical and cultural icon, blending mostly reggae, ska, and rocksteady in his compositions.", "body_of_works": 13},
#     {"name": "Billie Holiday", "instrument": "Vocals", "genre": "Jazz", "bio": "An American jazz and swing music singer with a career spanning nearly thirty years, Billie Holiday had a profound influence on jazz music and pop singing.", "body_of_works": 12},
#     {"name": "Aretha Franklin", "instrument": "Piano", "genre": "Soul", "bio": "Known as the 'Queen of Soul', Aretha Franklin was an American singer, songwriter, and pianist known for her powerful voice and emotional delivery.", "body_of_works": 38},
#     {"name": "Claude Debussy", "instrument": "Piano", "genre": "Classical", "bio": "A French composer, Debussy is considered one of the most influential composers of the late 19th and early 20th centuries, known for his use of non-traditional scales and chromaticism.", "body_of_works": 31},  # Compositions
#     {"name": "Dolly Parton", "instrument": "Guitar", "genre": "Country", "bio": "An American singer, songwriter, and businesswoman, Dolly Parton is known for her work in country music and has composed over 3,000 songs.", "body_of_works": 50},
#     {"name": "Daft Punk", "instrument": "Synthesizer", "genre": "Electronic", "bio": "A French electronic music duo widely regarded as one of the most influential acts in dance music history, known for their use of visual components and disguises.", "body_of_works": 4},
#     {"name": "Shakira", "instrument": "Vocals", "genre": "Pop", "bio": "Colombian singer, songwriter, dancer, and record producer, Shakira is noted for her musical versatility that incorporates elements from multiple genres and cultures.", "body_of_works": 11},
#     {"name": "Ennio Morricone", "instrument": "Orchestrator", "genre": "Film Score", "bio": "An Italian composer, orchestrator, conductor, and former trumpet player who wrote music in a wide range of musical styles, Morricone is considered one of the most influential and best-selling film composers of all time.", "body_of_works": 400},  # Film scores and albums
#     {"name": "B.B. King", "instrument": "Guitar", "genre": "Blues", "bio": "Known as the King of the Blues, B.B. King was an American blues singer, electric guitarist, songwriter, and record producer.", "body_of_works": 43},
#     {"name": "Björk", "instrument": "Vocals", "genre": "Alternative", "bio": "An Icelandic singer, songwriter, composer, actress, and DJ, Björk is known for her eclectic music style that draws on influences from a range of genres.", "body_of_works": 10}
# ]

# Create your views here.
def home(request):
    return render(request, 'musicians/home.html')

def about(request):
    return render(request, 'musicians/about.html')

def musicians_index(request):
    musicians = Musician.objects.all()
    return render(request, 'musicians/index.html', {
        'musicians': musicians
    })

def musicians_detail(request, musician_id):
    musician = Musician.objects.get(id=musician_id)
    return render(request, 'musicians/detail.html', {
        'musicians': musician
    })

# Class-based views
# CreateView, UpdateView, DeleteView
# These views are used to create, update, and delete objects respectively.
class MusicianCreate(CreateView):
    model = Musician
    fields = ['name', 'instrument', 'genre', 'bio', 'body_of_works']

class MusicianUpdate(UpdateView):
    model = Musician
    fields = ['instrument', 'genre', 'bio', 'body_of_works']

class MusicianDelete(DeleteView):
    model = Musician
    success_url = '/musicians/'