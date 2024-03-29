# Generated by Django 2.2.7 on 2019-11-09 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ImagineCode', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='box_id',
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='BoxToBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('box1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='boxtobox_requests_created', to='ImagineCode.Box')),
                ('box2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ImagineCode.Box')),
            ],
        ),
    ]
