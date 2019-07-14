from rest_framework import serializers

from polls.models import MyUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username','email','sex','career')


