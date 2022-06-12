from rest_framework.routers import SimpleRouter

from core.views import ProdutosViewSet, CategoriasViewSet, FornecedoresViewSet, FornecedorProdutoViewSet

router = SimpleRouter()
router.register('produtos', ProdutosViewSet)
router.register('categorias', CategoriasViewSet)
router.register('fornecedor', FornecedoresViewSet)
router.register('fornecedores', FornecedorProdutoViewSet)