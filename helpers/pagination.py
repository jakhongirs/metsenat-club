from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = "size"
    page_size = 10

    def get_paginated_response(self, data):
        return Response(
            {
                "page_size": self.get_page_size(self.request),
                "current_page": self.page.number,
                "total_pages": self.page.paginator.num_pages,
                "page_items": len(self.page),
                "total": self.page.paginator.count,
                "results": data,
            }
        )


class ByOne(CustomPagination):
    page_size = 1


class PageThree(CustomPagination):
    page_size = 3


class Short(CustomPagination):
    page_size = 4


class PageFive(CustomPagination):
    page_size = 5


class PageSix(CustomPagination):
    page_size = 6


class PageSeven(CustomPagination):
    page_size = 7


class DoubleShort(CustomPagination):
    page_size = 8


class MidShort(CustomPagination):
    page_size = 9


class ExtraShort(CustomPagination):
    page_size = 10


class Middle(CustomPagination):
    page_size = 12


class ExtraMiddle(CustomPagination):
    page_size = 15


class PageSixteen(CustomPagination):
    page_size = 16


class Twenty(CustomPagination):
    page_size = 20
