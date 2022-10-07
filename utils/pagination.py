import math
from django.core.paginator import Paginator


def makePaginationInfo(totalRange, tinySizeRange, currentPage):
    tinyRangeMiddle = math.ceil(tinySizeRange / 2)
    tinyRangeStart = currentPage - tinyRangeMiddle
    tinyRangeEnd = currentPage + tinyRangeMiddle

    totalSize = len(totalRange)
    offsetStart = abs(tinyRangeStart)

    if tinyRangeStart < 0:
        tinyRangeStart = 0
        tinyRangeEnd += offsetStart

    if tinyRangeEnd >= totalSize:
        tinyRangeStart = tinyRangeStart - abs(totalSize - tinyRangeEnd)

    tinyRange = totalRange[tinyRangeStart:tinyRangeEnd]

    return {
        'tinyRange': tinyRange,
        'totalRange': totalRange,
        'tinySizeRange': tinySizeRange,
        'currentPage': currentPage,
        'totalSize': totalSize,
        'rangeStart': tinyRangeStart,
        'rangeEnd': tinyRangeEnd,
        'isFirstPageNotInRange': currentPage > tinyRangeMiddle,
        'isLastPageNotInRange': tinyRangeEnd < totalSize
    }


def makePagination(request, querySet, qtyPerPage):
    try:
        requestPage = int(request.GET.get('page', 1))
    except ValueError:
        requestPage = 1

    paginator = Paginator(querySet, qtyPerPage)
    page = paginator.get_page(requestPage)

    paginationInfo = makePaginationInfo(paginator.page_range, 4, requestPage)
    return page, paginationInfo
