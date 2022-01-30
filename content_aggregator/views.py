from django.shortcuts import render, redirect
from random import shuffle
from content_aggregator.models import *
from view_generators import *
import feedparser

# Create your views here.


def subject_index(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'home.html', context)


def updatecovid(request):
    CovidContent.objects.all().delete()
    covidcontent = CovidContent.objects.all()
    content_list = []

    medium_url = feedparser.parse("https://medium.com/feed/tag/covid")
    for info in medium_url.entries:
        medium_view_generator(info, CovidContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/Coronavirus/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, CovidContent(), content_list)

    ecdc1_url = feedparser.parse("https://www.ecdc.europa.eu/en/taxonomy/term/2942/feed")
    for info in ecdc1_url.entries:
        default_view_generator(info, CovidContent(), content_list)

    ecdc2_url = feedparser.parse("https://www.ecdc.europa.eu/en/taxonomy/term/1310/feed")
    for info in ecdc2_url.entries:
        default_view_generator(info, CovidContent(), content_list)

    ecdc3_url = feedparser.parse("https://www.ecdc.europa.eu/en/taxonomy/term/1505/feed")
    for info in ecdc3_url.entries:
        default_view_generator(info, CovidContent(), content_list)

    shuffle(content_list)

    for i in content_list:
        i.save()

    context = {'covidcontent': covidcontent}

    return render(request, 'covidnews.html', context)


def updategaming(request):
    GamingContent.objects.all().delete()
    gamingcontent = GamingContent.objects.all()
    content_list = []

    medium_url = feedparser.parse("https://medium.com/feed/tag/gaming")
    for info in medium_url.entries:
        medium_view_generator(info, GamingContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/gaming/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, GamingContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/Games/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, GamingContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/pcgaming/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, GamingContent(), content_list)

    shuffle(content_list)

    for i in content_list:
        i.save()

    context = {'gamingcontent': gamingcontent}

    return render(request, 'gaming.html', context)


def updatenews(request):
    NewsContent.objects.all().delete()
    newscontent = NewsContent.objects.all()
    content_list = []

    medium_url = feedparser.parse("https://medium.com/feed/tag/news")
    for info in medium_url.entries:
        medium_view_generator(info, NewsContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/news/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, NewsContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/worldnews/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, NewsContent(), content_list)

    bbc_url = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml")
    for info in bbc_url.entries:
        default_view_generator(info, NewsContent(), content_list)

    cbn_url = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml")
    for info in cbn_url.entries:
        default_view_generator(info, NewsContent(), content_list)

    shuffle(content_list)

    for i in content_list:
        i.save()

    context = {'newscontent': newscontent}

    return render(request, 'worldnews.html', context)


def updateprogramming(request):
    ProgrammingContent.objects.all().delete()
    programmingcontent = ProgrammingContent.objects.all()
    content_list = []

    medium_url = feedparser.parse("https://medium.com/feed/tag/programming")
    for info in medium_url.entries:
        medium_view_generator(info, ProgrammingContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/programming/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, ProgrammingContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/webdev/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, ProgrammingContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/Coding/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, ProgrammingContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/JavaScript/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, ProgrammingContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/Python/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, ProgrammingContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/Java/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, ProgrammingContent(), content_list)

    shuffle(content_list)

    for i in content_list:
        i.save()

    context = {'programmingcontent': programmingcontent}

    return render(request, 'programming.html', context)


def updatescience(request):
    ScienceContent.objects.all().delete()
    sciencecontent = ScienceContent.objects.all()
    content_list = []

    medium_url = feedparser.parse("https://medium.com/feed/tag/science")
    for info in medium_url.entries:
        medium_view_generator(info, ScienceContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/science/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, ScienceContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/Futurology/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, ScienceContent(), content_list)

    sciencedaily_url = feedparser.parse("https://www.sciencedaily.com/rss/top/science.xml")
    for info in sciencedaily_url.entries:
        default_view_generator(info, ScienceContent(), content_list)

    shuffle(content_list)

    for i in content_list:
        i.save()

    context = {'sciencecontent': sciencecontent}

    return render(request, 'science.html', context)


def updatetech(request):
    TechContent.objects.all().delete()
    techcontent = TechContent.objects.all()
    content_list = []

    medium_url = feedparser.parse("https://medium.com/feed/tag/technology")
    for info in medium_url.entries:
        medium_view_generator(info, TechContent(), content_list)

    reddit_url = feedparser.parse("https://reddit.com/r/technology/.rss")
    for info in reddit_url.entries:
        reddit_view_generator(info, TechContent(), content_list)

    ndtv_url = feedparser.parse("https://gadgets.ndtv.com/rss/news")
    for info in ndtv_url.entries:
        default_view_generator(info, TechContent(), content_list)

    shuffle(content_list)

    for i in content_list:
        i.save()

    context = {'techcontent': techcontent}

    return render(request, 'technology.html', context)


def polskie(request):
    Polskie.objects.all().delete()
    polskie = Polskie.objects.all()
    content_list = []

    polsat_url = feedparser.parse("https://www.polsatnews.pl/rss/polska.xml")
    for info in polsat_url.entries:
        pl_view_generator(info, Polskie(), content_list)

    shuffle(content_list)

    for i in content_list:
        i.save()

    context = {'polskie': polskie}

    return render(request, 'polskie.html', context)


def swiatowe(request):
    Swiat.objects.all().delete()
    swiatowe = Swiat.objects.all()
    content_list = []

    polsat_url = feedparser.parse("https://www.polsatnews.pl/rss/swiat.xml")
    for info in polsat_url.entries:
        pl_view_generator(info, Swiat(), content_list)

    shuffle(content_list)

    for i in content_list:
        i.save()

    context = {'swiatowe': swiatowe}

    return render(request, 'swiatowe.html', context)
