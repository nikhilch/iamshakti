from rest_framework import serializers
from iamshakti.models import JTMUser

class JTMUserSerializer(serializers.Serializer):
    class Meta:
        model = JTMUser
        fields = ('firstName', 'lastName', 'email', 'interests', 'joindate', 'memberType')
