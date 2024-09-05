# Generated by Django 5.0.3 on 2024-05-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('Doctor care', 'Doctor care'), ('Nursing care', 'Nursing care'), ('Medical social services', 'Medical social services'), ('Homemaker or basic assistance care', 'Homemaker or basic assistance care')], default='Doctor care', max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(choices=[('5 PM', '5 PM'), ('5:30 PM', '5:30 PM'), ('6 PM', '6 PM'), ('6:30 PM', '6:30 PM'), ('7 PM', '7 PM'), ('7:30 PM', '7:30 PM'), ('8 PM', '8 PM'), ('8:30 PM', '8:30 PM'), ('9 PM', '9 PM'), ('9:30 PM', '9:30 PM')], default='3 PM', max_length=10),
        ),
    ]
