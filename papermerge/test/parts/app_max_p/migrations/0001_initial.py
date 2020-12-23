# Generated by Django 3.1 on 2020-11-05 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0029_auto_20201023_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_ptr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_max_p_document_related', related_query_name='app_max_p_documents', to='core.document')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
