# Generated by Django 4.2.1 on 2023-05-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chatbot", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="chat",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AddIndex(
            model_name="chat",
            index=models.Index(
                fields=["-created_at"], name="chatbot_cha_created_fc4e77_idx"
            ),
        ),
    ]
