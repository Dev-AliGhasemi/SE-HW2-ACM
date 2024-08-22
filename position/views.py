from http import HTTPStatus

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response

from position.models import Position
from position.serializers import PositionSerializer


class PositionList(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionDetail(RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionApply(UpdateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def patch(self, request, *args, **kwargs):
        user = request.user
        position_id = kwargs['pk']
        print(position_id)
        print(user)
        try:
            position = Position.objects.get(id=position_id)
            position.employee.add(user)
            position.save()
            return Response({}, HTTPStatus.OK)
        except Position.DoesNotExist:
            return Response({}, HTTPStatus.NOT_FOUND)


class PositionDecline(UpdateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def patch(self, request, *args, **kwargs):
        user = request.user
        position_id = kwargs['pk']
        print(position_id)
        print(user)
        try:
            position = Position.objects.get(id=position_id)
            position.employee.remove(user)
            position.save()
            return Response({}, HTTPStatus.OK)
        except Position.DoesNotExist:
            return Response({}, HTTPStatus.NOT_FOUND)
