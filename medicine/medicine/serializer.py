from rest_framework import serializers
from medicine_data.models import KoreanData, ForeignData

class KoreanSerializer(serializers.ModelSerializer):
    class Meta:
        model = KoreanData
        fields =('name','type','effective_ingredient','ei_amount')

class ForeignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignData
        fields =('id','name','dosage_form','ingredients','effective_ingredient','ei_amount')
