from django.contrib import admin
from baslerbauer_main.models import *

admin.site.register(Producer)
admin.site.register(Product)
admin.site.register(Consumer)
admin.site.register(Stock)
admin.site.register(Transaction)
admin.site.register(TransactionGroupCounter)

