from django.contrib import admin
from users.models import User, Friendship
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
admin.site.register(Friendship)
# Register your models here.
