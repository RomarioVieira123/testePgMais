from django.contrib import admin
from telephone_operator.models import TelephoneOperator


class TelephoneOperatorAdmin(admin.ModelAdmin):
    pass


admin.site.register(TelephoneOperator, TelephoneOperatorAdmin)
