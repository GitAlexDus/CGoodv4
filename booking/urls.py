from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage, ResaList, ResaUpdate, DeleteView, ResaPlacard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', ResaList.as_view(), name='resas'),
    path('resa-update/<int:pk>/', ResaUpdate.as_view(), name='resa-update'),
    path('resa-delete/<int:pk>/', DeleteView.as_view(), name='resa-delete'),

    #Resa-create
    path('resa-select/', ResaPlacard.as_view(), name='resa-create'),
    path('resa-select/<int:Placard_id>/', views.SelectCasier, name='resa-select-casier'),
    path('resa-select/placad/<int:Casier_id>/', views.ResaFinish, name='resa-finish'),

	path('pincheck/<int:Casier_id>/', views.get_Pin, name='get-pin'),

]
