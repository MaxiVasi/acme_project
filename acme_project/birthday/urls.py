from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    # path('', views.birthday, name='create'),
    # Использование CBV маршрут связывают с CBV: имя_класса.as_view()
    path('', views.BirthdayCreateView.as_view(), name='create'),
    # path('list/', views.birthday_list, name='list'),
    # Использование CBV маршрут связывают с CBV: имя_класса.as_view()
    path('list/', views.BirthdayListView.as_view(), name='list'),
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    # path('<int:pk>/edit/', views.birthday, name='edit'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    # path('<int:pk>/delete/', views.delete_birthday, name='delete'),
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
    path('<int:pk>/comment/', views.CongratulationCreateView.as_view(), name='add_comment'),
]
