# Generated by Django 3.0.6 on 2020-07-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShorter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=1024, verbose_name='Url')),
                ('url_short', models.CharField(max_length=6, unique=True)),
                ('count', models.IntegerField(default=0)),
                ('is_expired', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Short Link',
                'verbose_name_plural': 'Short Links',
                'ordering': ('-created_at',),
            },
        ),
    ]
