from django.urls import path
from app_teacher.views import login, home, register, api_result, api_result_id
from app_teacher import views


urlpatterns = [
    path(route='', view=home, name=""),
    path(route='home/', view=home, name="home"),
    path(route='receipt_list/', view=views.ReceiptListView.as_view(), name='receipt_list'),
    path(route='home/<str:filter_category>/', view=home, name="home"),

    path(route='receipt/create/', view=views.receipt_create, name="receipt_create"),
    path(route='receipt/<int:receipt_id>/', view=views.receipt, name="receipt"),
    path(route='receipt/<int:receipt_id>/delete/', view=views.receipt_delete, name="receipt_delete"),
    path(route='receipt/<int:receipt_id>/comment_create/', view=views.receipt_comment_create, name="receipt_comment_create"),
    path(route='receipt/<int:comment_id>/comment_delete/', view=views.receipt_comment_delete, name="receipt_comment_delete"),
    path(route='receipt/<int:receipt_id>/like_create/', view=views.receipt_like_create, name="receipt_like_create"),

    path(route='login/', view=login, name="login"),
    path(route='register/', view=register, name="register"),

    # читаем все рецепты
    path(route='api/result/', view=api_result, name="api_result"),

    # читаем рецепт по id
    path(route='api/result/<int:recept_id>/', view=api_result_id, name="api_result_id"),
]
