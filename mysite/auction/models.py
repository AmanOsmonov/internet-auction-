
from django.db import models
from django.contrib.auth.models import User

class Auction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_time = models.DateTimeField()
    image = models.ImageField(upload_to='auction_images/')
    current_bid=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    def __str__(self):
        return self.title




class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Bid on {self.auction.title} by {self.user.username}'
# Create your models here.
