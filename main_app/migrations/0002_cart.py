# Generated by Django 2.2.3 on 2019-07-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Code', models.CharField(max_length=10)),
                ('Price', models.CharField(max_length=5)),
                ('Quantity', models.FloatField(max_length=2)),
            ],
        ),
    ]
