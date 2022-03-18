from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, Http404, HttpResponse
import random
from string import ascii_letters, digits
from .models import Shortened


def index(request):
    return render(request, 'shortener/index.html')


# generates random combination of 10 chars
def gen_url(avail=ascii_letters + digits, size=10):
    return "".join([random.choice(avail) for i in range(size)])


# Check if URL has previously been created
def check_url(request, inurl):
    """
    Check if URL has already been shortened before
    If it exists, return the already shortened URL
    Otherwise, generate shortened URLs till we get a unique one
    """
    if Shortened.objects.filter(long=inurl).exists():
        new_shortened = Shortened.objects.get(long=inurl)
        return JsonResponse({'shortened_url': request.build_absolute_uri('/') + new_shortened.short})

    else:
        new_shortened = Shortened.objects.create(long=inurl, short=gen_url())
        while Shortened.objects.filter(short=new_shortened.short).exists():
            new_shortened.short = gen_url()
        new_shortened.save()
        return JsonResponse({'shortened_url': request.build_absolute_uri('/') + new_shortened.short})


def redirect_to_og(request, shortened_url):
    if Shortened.objects.filter(short=shortened_url).exists():
        og = Shortened.objects.get(short=shortened_url)
        return HttpResponseRedirect('https://' + og.long)

    else:
        raise Http404('Broken Link :(')