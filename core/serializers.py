from rest_framework import serializers

from core.models import Produto, Categoria, Usuario, Fornecedor, FornecedorProduto


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'senha': {'write_only': True}
        }
        model = Usuario
        fields = (
            'id',
            'nomeUsuario',
            'email',
            'senha',
            'admin'
        )


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Categoria
        fields = (
            'id',
            'nomeCategoria'
        )


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Produto
        fields = (
            'id',
            'nomeProduto',
            'codigo',
            'categoria',
            'valor',
            'quantidade',
        )


class FornecedorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Fornecedor
        fields = (
            'id',
            'nomeFornecedor',
        )


class FornecedorProdutoSerializer(serializers.ModelSerializer):

    class Meta:

        model = FornecedorProduto
        fields = (
            'id',
            'fornecedor',
            'produto'
        )