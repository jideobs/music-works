# Generated by Django 4.0.3 on 2022-04-11 06:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('title_slug', models.CharField(max_length=200)),
                ('iswc', models.CharField(max_length=11, null=True, unique=True)),
                ('iswc_slug', models.CharField(max_length=11, null=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('contributors', models.ManyToManyField(to='aggregator.contributor')),
            ],
        ),
    ]
