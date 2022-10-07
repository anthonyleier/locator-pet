import math
from django.core.paginator import Paginator


def montarRangePaginacao(page_range, qtd_paginas, pagina_atual):
    meio = math.ceil(qtd_paginas / 2)
    inicio = pagina_atual - meio
    fim = pagina_atual + meio
    total = len(page_range)

    inicio_offset = abs(inicio)

    if inicio < 0:
        inicio = 0
        fim += inicio_offset

    if fim >= total:
        inicio = inicio - abs(total - fim)

    paginacao = page_range[inicio:fim]
    return {
        'paginacao': paginacao,
        'page_range': page_range,
        'qtd_paginas': qtd_paginas,
        'pagina_atual': pagina_atual,
        'total': total,
        'inicio': inicio,
        'fim': fim,
        'primeira_pagina_tela': pagina_atual > meio,
        'ultima_pagina_tela': fim < total
    }


def construirPaginacao(request, querySet, quantidade):
    try:
        paginaDesejada = int(request.GET.get('page', 1))
    except ValueError:
        paginaDesejada = 1

    paginator = Paginator(querySet, quantidade)
    pagina = paginator.get_page(paginaDesejada)
    paginacao = montarRangePaginacao(paginator.page_range, 4, paginaDesejada)

    return pagina, paginacao
