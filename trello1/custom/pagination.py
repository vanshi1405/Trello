from rest_framework.pagination import PageNumberPagination, BasePagination


class CustomPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10
    page_size_query_param = 'page_size'

