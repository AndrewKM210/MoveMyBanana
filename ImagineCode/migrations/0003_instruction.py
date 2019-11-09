# Generated by Django 2.2.7 on 2019-11-09 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ImagineCode', '0002_auto_20191109_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ImagineCode.Box')),
            ],
        ),
    ]
