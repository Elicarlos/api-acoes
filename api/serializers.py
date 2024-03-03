from rest_framework import serializers
from api.models import FundoImobiliarios



class FundoImobiliarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = FundoImobiliarios
        fields = '__all__'
        # fields = ['id', 'codigo', 'setor', 'dividend_yeld_medio_12m', 'vancancia_financeira', 'vacancia_fisica', 'quantidade_ativos']