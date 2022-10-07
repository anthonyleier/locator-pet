from unittest import TestCase
from utils.pagination import makePaginationInfo


class PaginationTest(TestCase):
    def test_make_simple_tiny_range(self):
        paginationInfo = makePaginationInfo(totalRange=list(range(1, 21)), tinySizeRange=4, currentPage=1)
        self.assertEqual([1, 2, 3, 4], paginationInfo.get('tinyRange'))

    def test_make_tiny_range_start(self):
        paginationInfo = makePaginationInfo(totalRange=list(range(1, 21)), tinySizeRange=4, currentPage=1)
        self.assertEqual([1, 2, 3, 4], paginationInfo.get('tinyRange'))

        paginationInfo = makePaginationInfo(totalRange=list(range(1, 21)), tinySizeRange=4, currentPage=2)
        self.assertEqual([1, 2, 3, 4], paginationInfo.get('tinyRange'))

        paginationInfo = makePaginationInfo(totalRange=list(range(1, 21)), tinySizeRange=4, currentPage=3)
        self.assertEqual([2, 3, 4, 5], paginationInfo.get('tinyRange'))

        paginationInfo = makePaginationInfo(totalRange=list(range(1, 21)), tinySizeRange=4, currentPage=4)
        self.assertEqual([3, 4, 5, 6], paginationInfo.get('tinyRange'))

    def test_make_tiny_range_middle(self):
        paginationInfo = makePaginationInfo(totalRange=list(range(1, 21)), tinySizeRange=4, currentPage=10)
        self.assertEqual([9, 10, 11, 12], paginationInfo.get('tinyRange'))

        paginationInfo = makePaginationInfo(totalRange=list(range(1, 21)), tinySizeRange=4, currentPage=15)
        self.assertEqual([14, 15, 16, 17], paginationInfo.get('tinyRange'))

    def test_make_tiny_range_end(self):
        paginationInfo = makePaginationInfo(totalRange=list(range(1, 21)), tinySizeRange=4, currentPage=18)
        self.assertEqual([17, 18, 19, 20], paginationInfo.get('tinyRange'))

        paginationInfo = makePaginationInfo(totalRange=list(range(1, 21)), tinySizeRange=4, currentPage=19)
        self.assertEqual([17, 18, 19, 20], paginationInfo.get('tinyRange'))

        paginationInfo = makePaginationInfo(totalRange=list(range(1, 21)), tinySizeRange=4, currentPage=20)
        self.assertEqual([17, 18, 19, 20], paginationInfo.get('tinyRange'))
