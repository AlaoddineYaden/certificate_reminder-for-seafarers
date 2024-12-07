# Generated by Django 5.1.3 on 2024-11-29 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_remove_person_user_person_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateField()),
                ('certificate_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.certificatetype')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='people.person')),
            ],
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
    ]
