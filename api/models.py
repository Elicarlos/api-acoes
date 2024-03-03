from django.db import models

import uuid

# Create your models here.

class FundoImobiliarios(models.Model):
    SETOR_CHOICES = [
    ('hospital', 'Hospital'), ('hotel', 'Hotel'), ('hibrido', 'Híbrido'),
    ('lajes_corporativas', 'Lajes Corporativas'), 
    ('logistica', 'Logística'), ('outros', 'Outros'), 
    ('residencial', 'Residencial'),
    ('titulos_valores_mobiliarios', 'Títulos e Val. Mob.')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=True)
    codigo = models.CharField(max_length=8, null=False, blank=False)
    setor = models.CharField(max_length=30, null=False, blank=False, choices=SETOR_CHOICES)
    dividend_yeald_medio_12m = models.DecimalField(null=True, blank=False, max_digits=5, decimal_places=2)
    vancancia_financeira = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    vacancia_fisica = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2 )
    quantidade_ativos = models.IntegerField(null=False, blank=False, default=0)

    


