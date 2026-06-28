from django.contrib import admin
from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autor',
        'categoria',
        'quantidade',
        'disponivel'
    )

    search_fields = (
        'titulo',
        'autor'
    )

    list_filter = (
        'categoria',
        'disponivel'
    )