# Generated by Django 3.1.3 on 2020-11-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.TextField(max_length=50)),
                ('message', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='myskill',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='myskill',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]