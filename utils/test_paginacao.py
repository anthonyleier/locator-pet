from unittest import TestCase
from utils.paginacao import montarRangePaginacao


class PaginationTest(TestCase):
    def test_montar_range(self):
        paginacao = montarRangePaginacao(page_range=list(range(1, 21)), qtd_paginas=4, pagina_atual=1)
        self.assertEqual([1, 2, 3, 4], paginacao.get('paginacao'))

    def test_range_fixo_se_pagina_menor_que_metade_range(self):
        # Atual = 1 - Meio = 2
        paginacao = montarRangePaginacao(page_range=list(range(1, 21)), qtd_paginas=4, pagina_atual=1)
        self.assertEqual([1, 2, 3, 4], paginacao.get('paginacao'))

        # Atual = 2 - Meio = 2
        paginacao = montarRangePaginacao(page_range=list(range(1, 21)), qtd_paginas=4, pagina_atual=2)
        self.assertEqual([1, 2, 3, 4], paginacao.get('paginacao'))

        # Atual = 3 - Meio = 2
        paginacao = montarRangePaginacao(page_range=list(range(1, 21)), qtd_paginas=4, pagina_atual=3)
        self.assertEqual([2, 3, 4, 5], paginacao.get('paginacao'))

        # Atual = 4 - Meio = 2
        paginacao = montarRangePaginacao(page_range=list(range(1, 21)), qtd_paginas=4, pagina_atual=4)
        self.assertEqual([3, 4, 5, 6], paginacao.get('paginacao'))

    def test_metade_range_correto(self):
        # Atual = 10 - Meio = 2
        paginacao = montarRangePaginacao(page_range=list(range(1, 21)), qtd_paginas=4, pagina_atual=10)
        self.assertEqual([9, 10, 11, 12], paginacao.get('paginacao'))

        # Atual = 15 - Meio = 2
        paginacao = montarRangePaginacao(page_range=list(range(1, 21)), qtd_paginas=4, pagina_atual=15)
        self.assertEqual([14, 15, 16, 17], paginacao.get('paginacao'))

    def test_fim_range_correto(self):
        # Atual = 18 - Meio = 2
        paginacao = montarRangePaginacao(page_range=list(range(1, 21)), qtd_paginas=4, pagina_atual=18)
        self.assertEqual([17, 18, 19, 20], paginacao.get('paginacao'))

        # Atual = 19 - Meio = 2
        paginacao = montarRangePaginacao(page_range=list(range(1, 21)), qtd_paginas=4, pagina_atual=19)
        self.assertEqual([17, 18, 19, 20], paginacao.get('paginacao'))

        # Atual = 20 - Meio = 2
        paginacao = montarRangePaginacao(page_range=list(range(1, 21)), qtd_paginas=4, pagina_atual=20)
        self.assertEqual([17, 18, 19, 20], paginacao.get('paginacao'))
