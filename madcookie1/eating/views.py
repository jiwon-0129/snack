from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count, Avg
from django.utils import timezone
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request):
    #paginator 페이지 분리
    eatings = Eating.objects.order_by('-pub_date')
        # 검색 기능
    # if request.method == 'GET':
    #     search_query = request.GET.get('search_box', "").text
    #     eatings = Eating.objects.filter((name_icontains=search_query)|Q(hashtag=search_query))
        # queryset = Eating.objects.filter(name__icontains=search_query)
        # queryset |= Eating.objects.filter(hashtag__icontains=search_query)
        # eatings = queryset
    

    paginator = Paginator(eatings, 5)
    page = request.GET.get('page', 1)
    eatings = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'home.html', {'eatings': eatings,'categories':categories})
    
def review(request, pk):
    snack=get_object_or_404(Eating, pk=pk)
    return render(request, 'review.html', {'snack': snack})

@login_required(login_url='/login/')
def edit(request, review_id):
    review_detail = get_object_or_404(Review, pk=review_id)
    return render(request, 'edit.html', {'review': review_detail})

def detail(request, review_id):
    review_detail = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review_detail})

@login_required(login_url='/login/')
def create(request):
    form= ReviewForm(request.POST, request.FILES)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.pub_date = timezone.now()
        new_review.save()
        return redirect('detail', new_review.id)
    return redirect('review')

@login_required(login_url='/login/')
def new(request):
    form = ReviewForm()
    return render(request, 'new.html', {'form':form})

@login_required(login_url='/login/')
def update(request, review_id):
    review_update = get_object_or_404(Review, pk = review_id)
    review_update.score= request.POST['score']
    review_update.image = request.POST['image']
    review_update.body = request.POST['body']
    review_update.pub_date = timezone.now()
    review_update.salty_taste = request.POST['salty_taste']
    review_update.sweet_taste = request.POST['sweet_taste']
    review_update.spicy_taste = request.POST['spicy taste']
    review_update.save()
    return redirect('review_datail')

@login_required(login_url='/account/login/')
def delete(request, review_id):
    review_delete = get_object_or_404(Review, pk=review_id)
    review_delete.delete()
    return redirect(request, 'review.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
        return redirect("home")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("home")
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def category(request, category_id):
    eatings = Eating.objects.filter(category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.all()
    return render(request, 'category.html', {'eatings': eatings,'category':category, 'categories':categories})

def total_rating(self): 
    all_reviews = self.reviews.all() 
    all_ratings = 0 
    for review in all_reviews: 
        all_ratings += review.rating_average() 
    return all_ratings/len(all_reviews)
