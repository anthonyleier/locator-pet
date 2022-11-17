import math
from django.core.paginator import Paginator


def makePaginationInfo(paginator, tinyRangeSize, currentPage):
    totalRange = paginator.page_range
    tinyRangeHalfSize = math.ceil(tinyRangeSize / 2)
    tinyRangeStart = currentPage - tinyRangeHalfSize
    tinyRangeEnd = currentPage + tinyRangeHalfSize

    totalSize = len(totalRange)
    offsetStart = abs(tinyRangeStart)

    if tinyRangeStart < 0:
        tinyRangeStart = 0
        tinyRangeEnd += offsetStart

    if tinyRangeEnd >= totalSize:
        tinyRangeStart = tinyRangeStart - abs(totalSize - tinyRangeEnd)

    tinyRange = totalRange[tinyRangeStart:tinyRangeEnd]

    return {
        'paginator': paginator,
        'tinyRange': tinyRange,
        'totalRange': totalRange,
        'tinySizeRange': tinyRangeSize,
        'currentPage': currentPage,
        'totalSize': totalSize,
        'rangeStart': tinyRangeStart,
        'rangeEnd': tinyRangeEnd,
        'isFirstPageNotInRange': currentPage > tinyRangeHalfSize,
        'isLastPageNotInRange': tinyRangeEnd < totalSize
    }


def makePagination(request, querySet, qtyPerPage):
    try:
        requestPage = int(request.GET.get('page', 1))

    except ValueError:
        print("Número de página inválida, redirecionando para a primeira")
        requestPage = 1

    paginator = Paginator(querySet, qtyPerPage)
    page = paginator.get_page(requestPage)

    paginationInfo = makePaginationInfo(paginator, 4, requestPage)
    return page, paginationInfo
