from .models import *
from rest_framework import serializers
from hanspell import spell_checker
from .utils import *
from .classes import *


class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Text
        fields = ('original', 'checked', 'errors')
        read_only_fields = ('checked',)

    def create(self, validated_data):
        spell_result = spell_checker.check(validated_data.get('original'))
        save_dict_word(spell_result.as_dict())
        validated_data['checked'] = spell_result.as_dict()['checked']
        validated_data['errors'] = spell_result.as_dict()['errors']
        return Text.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class ResponseSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    chat_id = serializers.IntegerField()
    checked = serializers.CharField(max_length=500)
    errors = serializers.IntegerField()
