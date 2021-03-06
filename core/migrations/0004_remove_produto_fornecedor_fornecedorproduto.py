# Generated by Django 4.0.4 on 2022-06-12 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_produto_fornecedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='fornecedor',
        ),
        migrations.CreateModel(
            name='FornecedorProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fornecedor')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produto')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
