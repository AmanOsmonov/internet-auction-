

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .forms import RegisterUserForm
from .models import Auction, Bid

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def home(request):
    auctions = Auction.objects.all()
    return render(request, 'home.html', {'auctions': auctions})


# Create your views here.

def auction_detail(request, auction_id):
    auction = Auction.objects.get(id=auction_id)

    return render(request, 'auction_detail.html', {"auction": auction})





@login_required
def place_bid(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    if request.method == 'POST':
        bid_amount = float(request.POST.get('bid_amount'))
        if bid_amount > auction.start_price:
            bid = Bid(auction=auction, user=request.user, amount=bid_amount)
            bid.save()

            if bid_amount > auction.current_bid:
                auction.current_bid = bid_amount
                auction.save()


    return redirect('auction_detail', auction_id=auction_id)


def create_auction(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('login')
