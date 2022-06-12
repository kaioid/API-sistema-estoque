from rest_framework import viewsets

from .models import Fornecedor, Produto, Categoria, FornecedorProduto
from .serializers import FornecedorSerializer, ProdutoSerializer, CategoriaSerializer, FornecedorProdutoSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class FornecedoresViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class FornecedorProdutoViewSet(viewsets.ModelViewSet):
    queryset = FornecedorProduto.objects.all()
    serializer_class = FornecedorProdutoSerializer
