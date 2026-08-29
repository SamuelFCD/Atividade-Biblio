from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Livro, Autor

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'data_lancamento')
    search_fields = ('titulo', 'editora')

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ano_nascimento')
    search_fields = ('nome',)

admin.site.register(Livro, LivroAdmin)
admin.site.register(Autor, AutorAdmin)