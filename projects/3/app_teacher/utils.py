from django.core.paginator import Paginator


class CustomPaginator:
    @staticmethod
    def get_page(objs: list, limit: int, current_page):
        if current_page is None:
            current_page = 1
        page = Paginator(objs, limit)
        return page.get_page(int(current_page))

    @staticmethod
    def get_page1(objs: list, limit: int, current_page: int):
        page = Paginator(objs, limit)
        return page.get_page(current_page)
