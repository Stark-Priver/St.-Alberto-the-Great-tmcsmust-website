# Generated by Django 4.2.15 on 2024-08-23 16:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('AuthenticationApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmcsmember',
            name='vyama_vya_kitume',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('LEGIO MARIA', 'LEGIO MARIA'), ('KARISMATIKI', 'KARISMATIKI'), ('KWAYA', 'KWAYA'), ('MOYO MTAKATIFU WA YESU', 'MOYO MTAKATIFU WA YESU'), ('WATUMISHI WA ALTARE', 'WATUMISHI WA ALTARE')], max_length=100, verbose_name='Utume'),
        ),
    ]
