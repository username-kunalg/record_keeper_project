from django.urls import path
from .views import *


urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('records/', RecordListView.as_view(), name='record_list'),
    path('records/create/', RecordCreateView.as_view(), name='record_create'),
    path('records/<int:pk>/edit/', RecordUpdateView.as_view(), name='record_edit'),
    path('records/<int:pk>/delete/', RecordDeleteView.as_view(), name='record_delete'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
