# Generated by Django 3.2.3 on 2021-06-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignData',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('dosage_form', models.TextField(blank=True, db_column='Dosage_form', null=True)),
                ('ingredients', models.TextField(blank=True, db_column='Ingredients', null=True)),
                ('effective_ingredient', models.TextField(blank=True, db_column='Effective_Ingredient', null=True)),
                ('ei_amount', models.TextField(blank=True, db_column='EI_Amount', null=True)),
            ],
            options={
                'db_table': 'foreign_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KoreanData',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('symptoms', models.TextField(blank=True, db_column='Symptoms', null=True)),
                ('how_to_take', models.TextField(blank=True, db_column='How_to_Take', null=True)),
                ('type', models.TextField(blank=True, db_column='Type', null=True)),
                ('ingredients', models.TextField(blank=True, db_column='Ingredients', null=True)),
                ('amount', models.TextField(blank=True, db_column='Amount', null=True)),
                ('effective_ingredient', models.TextField(blank=True, db_column='Effitive_Ingredient', null=True)),
                ('ei_amount', models.TextField(blank=True, db_column='EI_Amount', null=True)),
                ('unit', models.TextField(blank=True, db_column='Unit', null=True)),
                ('additives', models.TextField(blank=True, db_column='Additives', null=True)),
            ],
            options={
                'db_table': 'korean_data',
                'managed': False,
            },
        ),
    ]