# Generated by Django 5.0.3 on 2024-03-09 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=20)),
                ('studentID', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
