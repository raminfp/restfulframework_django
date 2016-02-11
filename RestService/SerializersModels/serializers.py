from rest_framework import serializers

from RestService.APIModel.SaminAPIModel import Samin


class SaminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Samin
        fields = ('Firstname', 'Lastname', 'Email','Address')
        # read_only_fields = ('Address',)

        def create(self, validated_data):

             user = Samin(
                email=validated_data['Email'],
                username=validated_data['Firstname']
             )
             user.set_password(validated_data['Address'])
             user.save()
             return user