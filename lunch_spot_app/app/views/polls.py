from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Poll
from ..serializer import PollSerializer


@api_view(["GET"])
def poll_results(request):
    poll = Poll.objects.all()
    if poll:
        serializer = PollSerializer(poll, many=True)
        return Response(serializer.data)
    else:
        return Response("No poll found", status=status.HTTP_404_NOT_FOUND)
