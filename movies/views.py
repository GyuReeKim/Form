from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
# from IPython import embed
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        # 데이터 검증이 되었을 때
        if form.is_valid():
            movie = Movie()
            movie.title = form.cleaned_data.get('title')
            movie.title_en = form.cleaned_data.get('title_en')
            movie.audience = form.cleaned_data.get('audience')
            movie.open_date = form.cleaned_data.get('open_date')
            movie.genre = form.cleaned_data.get('genre')
            movie.watch_grade = form.cleaned_data.get('watch_grade')
            movie.score = form.cleaned_data.get('score')
            movie.poster_url = form.cleaned_data.get('poster_url')
            movie.description = form.cleaned_data.get('description')
            movie.save()
            return redirect('movies:index')
        # 데이터 검증이 되지 않았을 때
        # else:
            # context = {
            #     'form': form,
            # }
            # return render(request, 'form.html', context)
            # pass
    else:
        # Create
        form = MovieForm()
        # context = {
        #     'form': form,
        # }
        # return render(request, 'form.html', context)
    # 공통된 부분이므로 밖으로 빼줄 수 있다.
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)

def detail(request, id):
    # movie = Movie.objects.get(id=id)
    # 사용자가 찾을수 없는 정보에 접근할 때 404페이지를 보여준다.
    movie = get_object_or_404(Movie, id=id)
    context = {
        'movie': movie,
    }
    return render(request, 'detail.html', context)

def delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        movie.delete()
        return redirect('movies:index')
    else:
        # GET요청이 들어오면 삭제시키지 않는다.
        return redirect('movies:detail', id)

def update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        pass
    else:
        form = MovieForm(initial=movie.__dict__) # initial에 원본 데이터를 넣어준다.
    # 사용자가 옳지 않게 저장했을 때 기존의 데이터를 불러오기 위해서 코드를 아래로 빼서 작성하였다.
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)