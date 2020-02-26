# Generated by Django 2.2.7 on 2020-02-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('desc', models.TextField()),
                ('price', models.TextField()),
                ('summary', models.TextField(default='this is summary')),
            ],
        ),
    ]
