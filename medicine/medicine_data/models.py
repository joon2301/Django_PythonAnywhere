from django.db import models

class ForeignData(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    dosage_form = models.TextField(db_column='Dosage_form', blank=True, null=True)  # Field name made lowercase.
    ingredients = models.TextField(db_column='Ingredients', blank=True, null=True)  # Field name made lowercase.
    effective_ingredient = models.TextField(db_column='Effective_Ingredient', blank=True, null=True)  # Field name made lowercase.
    ei_amount = models.TextField(db_column='EI_Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foreign_data'

class KoreanData(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    symptoms = models.TextField(db_column='Symptoms', blank=True, null=True)  # Field name made lowercase.
    how_to_take = models.TextField(db_column='How_to_Take', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    ingredients = models.TextField(db_column='Ingredients', blank=True, null=True)  # Field name made lowercase.
    amount = models.TextField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    effective_ingredient = models.TextField(db_column='Effective_Ingredient', blank=True, null=True)  # Field name made lowercase.
    ei_amount = models.TextField(db_column='EI_Amount', blank=True, null=True)  # Field name made lowercase.
    unit = models.TextField(db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    additives = models.TextField(db_column='Additives', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'korean_data'
