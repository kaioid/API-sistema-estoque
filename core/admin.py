from django.contrib import admin

from .models import *


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["nomeUsuario"]


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nomeCategoria"]


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["nomeProduto", "categoria", "quantidade"]


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ["nomeFornecedor"]


@admin.register(FornecedorProduto)
class FornecedorProdutoAdmin(admin.ModelAdmin):
    list_display = ["fornecedor", "produto"]
