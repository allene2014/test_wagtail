# Generated by Django 4.0.4 on 2022-06-03 04:41

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_oriente_orientepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='orientepage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
