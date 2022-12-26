from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm) # icontains: case insensitive
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})

def about(request):
    return HttpResponse("<h1>Welcome to the about page</h1>")

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk = movie_id) # get the movie object from the database
    reviews = Review.objects.filter(movie = movie) # get all the reviews for the movie
    return render(request, 'detail.html',
                    {'movie': movie, 'reviews': reviews}) # pass the movie and reviews to the template
@login_required
def createreview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id) # get the movie object from the database
    """
        When receve a GET request, it means that user is navigating to the createreview page,
        and we render createreview.html and pass in the review form for the user to create the
        review.
    """
    if request.method == 'GET':
        return render(request, 'createreview.html', {'form': ReviewForm(), 'movie': movie})
    else:
        try:
            form = ReviewForm(request.POST) # retrieve the form for the request
            newReview = form.save(commit=False)
            
            # we specify the user and movie relationships for the review
            newReview.user = request.user
            newReview.movie = movie

            newReview.save() # save review in the database

            return redirect('detail', newReview.movie.id)

        except ValueError:
            return render(request, 'createreview.html', {'form': ReviewForm(), 'error': 'bad data passed in. Try again'})

@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user) # get the review object from the database
    if request.method == 'GET': # if the request is a GET request, then we render the updatereview.html template    
        form = ReviewForm(instance=review) # create a form with the review data
        return render(request, 'updatereview.html', 
                        {'review': review, 'form': form}) 
    else:
        try:
            form = ReviewForm(request.POST, instance=review) # create a form with the review data
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            return render(request, 'updatereview.html',
                            {'review': review, 'form': form, 'error': 'Bad data in form. Try again'})

@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user) # get the review object from the database
    review.delete()
    return redirect('detail', review.movie.id)