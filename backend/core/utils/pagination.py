from rest_framework.pagination import PageNumberPagination


class StandardPageNumberPagination(PageNumberPagination):
    """Standard page number pagination"""
    page_size_query_param = 'page_size'
    page_size = 10
