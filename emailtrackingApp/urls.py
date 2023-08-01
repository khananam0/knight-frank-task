from django.urls import path
from . import views

urlpatterns = [
      path('compose_email/',views.compose_email, name='compose_email'),
      path('image/<int:id>', views.image, name='image'),
      path('all_user_email/', views.all_user_email, name = "all_user_email"),
      path("multimail/", views.multimail, name = "multimail")
]


