from rest_framework import serializers

from rest_service.models import Samin


class SaminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Samin
        fields = ('firstname', 'lastname', 'email','address')
        # read_only_fields = ('Address',)

        def create(self, validated_data):

            user = Samin(
                email=validated_data['email'],
                username=validated_data['firstname']
            )
            user.set_password(validated_data['address'])
            user.save()
            return user

