from django.contrib import admin
from broker.models import Broker


class BrokerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Broker, BrokerAdmin)
