# Generated by Django 5.1.2 on 2024-10-25 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_type', models.CharField(choices=[('operator', 'Operator'), ('operand', 'Operand')], max_length=8)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('left', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left_child', to='rules.node')),
                ('right', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_child', to='rules.node')),
            ],
        ),
    ]
