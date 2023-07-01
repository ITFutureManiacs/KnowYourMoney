# Generated by Django 4.2.2 on 2023-07-01 08:39

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("budget_manager", "0002_category_rename_currencies_currency_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="cost",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=7,
                validators=[
                    django.core.validators.MinValueValidator(
                        0.01, "Wartość musi być większa od 0"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="expense",
            name="currency",
            field=models.ForeignKey(
                default=False,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="budget_manager.currency",
            ),
        ),
        migrations.AlterField(
            model_name="expense",
            name="expense_date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name="income",
            name="amount",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=7,
                validators=[
                    django.core.validators.MinValueValidator(
                        0.01, "Wartość musi być większa od 0"
                    )
                ],
            ),
        ),
    ]
