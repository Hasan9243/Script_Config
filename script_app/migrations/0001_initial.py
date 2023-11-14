# Generated by Django 4.2.6 on 2023-10-09 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='info_portal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interface_Number', models.CharField(max_length=1000)),
                ('VLAN', models.CharField(max_length=1000)),
                ('Description', models.CharField(max_length=1000)),
                ('IP_Address', models.CharField(max_length=1000)),
                ('Subnet_Mask', models.CharField(max_length=1000)),
                ('Network_Address', models.CharField(max_length=1000)),
                ('Network_Mask', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='VRF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VRF_Name', models.CharField(choices=[('ABBL_Intra_Br', 'ABBL_Intra_Br'), ('IBBL_Intra', 'IBBL_Intra'), ('PUBALI_Intra', 'PUBALI_Intra')], default='ABBL_Intra_Br', max_length=100)),
                ('Interface_Number', models.CharField(max_length=1000)),
                ('VLAN_Number', models.CharField(max_length=1000)),
                ('Description', models.CharField(max_length=1000)),
                ('IP_Address', models.CharField(max_length=1000)),
                ('Subnet_Mask', models.CharField(max_length=1000)),
                ('Netowrk_Address', models.CharField(max_length=1000)),
                ('Netowrk_Mask', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=1000)),
                ('designation', models.CharField(max_length=1000)),
                ('department', models.CharField(max_length=1000)),
                ('profile_pic', models.ImageField(blank=True, upload_to='pp')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]