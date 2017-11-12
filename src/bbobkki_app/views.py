from django.shortcuts import render,redirect
from .models import GuessNumbers
from .forms import PostForm

def detail(request, pk):
    
    lotto = GuessNumbers.objects.get(pk=pk)
    context = {
        "lotto" : lotto
    }

    return render(request, "bbobkki_app/lotto_detail.html", context)


def index(request):
    
    lottos = GuessNumbers.objects.all()
    context = {
        "lottos" : lottos
    }

    return render(request,"bbobkki_app/index.html",context)


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')
    else:
        
        form = PostForm()
        return render(request,"bbobkki_app/lotto_new.html",{"form":form})