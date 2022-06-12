from django.db import models


class Usuario(models.Model):

    nomeUsuario = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=45, unique=True)
    senha = models.CharField(max_length=45)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nomeUsuario

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['id']


class Fornecedor(models.Model):

    nomeFornecedor = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.nomeFornecedor

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['id']


class Categoria(models.Model):

    nomeCategoria = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['id']

    def __str__(self):
        return self.nomeCategoria


class Produto(models.Model):

    nomeProduto = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    valor = models.FloatField()
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return self.nomeProduto

    class Meta:

        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['id']


class FornecedorProduto(models.Model):

    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    class Meta:

        ordering = ['id']
