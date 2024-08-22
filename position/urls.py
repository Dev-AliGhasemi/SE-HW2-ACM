from django.urls import path
from position.views import PositionList, PositionDetail, PositionApply, PositionDecline

urlpatterns = [
    path("", PositionList.as_view()),
    path("<int:pk>", PositionDetail.as_view()),
    path("apply/<int:pk>", PositionApply.as_view()),
    path("decline/<int:pk>", PositionDecline.as_view()),

]
