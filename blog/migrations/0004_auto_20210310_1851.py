# Generated by Django 3.1.5 on 2021-03-10 15:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210224_0332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]