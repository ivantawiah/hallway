from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Testimony
from .models import Team
from .models import MostFeaturedArticle
from .models import HallwayEvent

# Create your views here.

def index (request):
    testimonies = Testimony.objects.all()
    team = Team.objects.all()
    return render(request, "index.html", {"testimon" : testimonies, "teams": team})

def generate_pdf(request):
    # Example context data
    context = {
        'title': 'Sample PDF',
        'content': 'This is a sample PDF generated using Django and html2pdf.js.',
    }
    return render(request, "digital_cert.html", context)

def brova (request):
    return HttpResponse("<h1> I LOVE YOU")

def blog(request):
    blog_two = MostFeaturedArticle.objects.all()
    blog_last = MostFeaturedArticle.objects.last()
    events = HallwayEvent.objects.all()
    all_content = [ MostFeaturedArticle, Team, Testimony]
    return render(request, 'blog.html', {"bogs": blog_two, "recent": blog_last, "all": all_content, "event": events})

def blog_two(request):
    blog_two = MostFeaturedArticle.objects.all()
    blog_last = MostFeaturedArticle.objects.last()
    events = HallwayEvent.objects.all()
    all_content = [ MostFeaturedArticle, Team, Testimony]
    return render(request, "blog_two.html", {"bogs": blog_two, "recent": blog_last, "all": all_content, "event": events})

def article(request, pk):
    return render(request, "article.html", {'pk': pk})

def register(request):

    if request.method == 'POST':
        businessname = request.POST['businessname']
        ownername = request.POST['ownername']
        tel = request.POST['tel']
        email = request.POST['email']
        address = request.POST['address']
        productlist = request.POST['productlist']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'There is an account with this email')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('index')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')
    

    
    
