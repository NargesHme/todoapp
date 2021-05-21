from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('submit',views.submit,name='submit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('list',views.list,name='list'),
    #path('sortdata',views.sortdata,name='sortdata'),
    path('searchdata',views.searchdata,name='searchdata'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('complete/<int:id>', views.complete, name='complete'),
    path('not_completed_list',views.not_completed_list,name='not_completed_list'),
    path('completed_list', views.completed_list, name='completed_list'),

]