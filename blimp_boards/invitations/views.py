from django.http import Http404

from rest_framework import generics
from rest_framework.response import Response

from ..utils.response import ErrorResponse
from ..utils.mixins import BulkCreateModelMixin
from ..utils.viewsets import ModelViewSet
from .models import SignupRequest, InvitedUser
from .serializers import (SignupRequestSerializer, InvitedUserSerializer,
                          InvitedUserFullSerializer)


class SignupRequestCreateAPIView(BulkCreateModelMixin, generics.CreateAPIView):
    model = SignupRequest
    serializer_class = SignupRequestSerializer
    authentication_classes = ()
    permission_classes = ()

    def post_save(self, obj, created=False):
        obj.send_email()


class InvitedUserCreateAPIView(generics.CreateAPIView):
    serializer_class = InvitedUserSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)

        if serializer.is_valid():
            serializer.send_invite()
            return Response(serializer.data)

        return ErrorResponse(serializer.errors)


class InvitedUserViewSet(ModelViewSet):
    model = InvitedUser
    serializer_class = InvitedUserFullSerializer
    authentication_classes = ()
    permission_classes = ()

    def get_object(self, queryset=None):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        lookup = self.kwargs.get(lookup_url_kwarg, None)

        obj = InvitedUser.objects.get_from_token(lookup)

        if not obj:
            raise Http404

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
