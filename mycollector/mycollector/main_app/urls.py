from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('tops/', views.top_index, name='index'),
    path("tops/<int:top_id>/", views.top_details, name='detail'),
    path("tops/create/", views.TopCreate.as_view(), name="tops_create"),
    path('tops/<int:pk>/update/', views.TopUpdate.as_view(), name = "tops_update"),
    path('tops/<int:pk>/delete/', views.TopDelete.as_view(), name = "tops_delete"),
    # path('tops/<int:top_id>/add_feeding/', views.add_feeding, name='add_feeding'),

    # Toys CRUD Operations
    path('pants/', views.PantsList.as_view(), name='pants_index'),
    path('pant/create/', views.PantCreate.as_view(), name='pants_create'),
    path('pants/<int:pants_id>/', views.PantsList.as_view(), name='pants_detail'),
    path('pants/<int:pk>/update/', views.PantsUpdate.as_view(), name='pants_update'),
    path('pants/<int:pk>/delete/', views.PantsDelete.as_view(), name='pants_delete'),

    # Asscociate a toy with Cat (M:M)
    path('tops/<int:top_id>/assoc_outfit/<int:pants_id>/', views.assoc_outfit, name = 'assoc_outfit'),
    # Unasscociate a toy with Cat (M:M)
    path('tops/<int:top_id>/assoc_outfit/<int:pants_id>/', views.unassoc_outfit, name='unassoc_outfit')
]