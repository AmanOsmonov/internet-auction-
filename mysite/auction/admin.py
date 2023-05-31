from django.contrib import admin
from .models import Auction, Bid

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_price','current_bid', 'end_time')
    list_filter = ('end_time',)
    search_fields = ('title', 'description')



class BidAdmin(admin.ModelAdmin):
    list_display = ('auction', 'user', 'amount', 'timestamp')
    list_filter = ('auction',)
    readonly_fields = ('timestamp',)

admin.site.register(Auction, AuctionAdmin)
admin.site.register(Bid, BidAdmin)
# Register your models here.
