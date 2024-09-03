from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken


from .models import Mobile, Brand

admin.site.unregister([BlacklistedToken, OutstandingToken])

admin.site.unregister(Group)

admin.site.register(Brand)

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):

    list_display = ['brand', 'model', 
                    'storage_capacity', 
                    'ram', 'mobile_type', 
                    'price', 'stock_quantity', 
                    'created_at'
                    ]
    list_filter = ['price', 'brand',
                   'model', 'stock_quantity',
                   'storage_capacity',
                   'ram', 'color',
                   'battery_capacity',
                   'mobile_type',
                   'processor',
                   ]
    search_fields = ['price', 'brand',
                    'model', 'network', 
                   'stock_quantity',
                   'storage_capacity',
                   'ram', 'color',
                   'battery_capacity',
                   'mobile_type',
                   'processor',
                   ]
    

