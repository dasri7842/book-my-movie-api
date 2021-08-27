from django.urls import path
from bookings import views

urlpatterns = [
    path('theatres/<int:theatre_id>/<int:show_id>/',
         views.SeatList.as_view()),
    path('booking/', views.BookTicket.as_view())
]
