# Generated by Django 4.1.3 on 2022-12-11 05:10

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Parcel = apps.get_model("manager", "Parcel")
    Address = apps.get_model("manager", "Address")
    Shipment = apps.get_model("manager", "Shipment")
    Commodity = apps.get_model("manager", "Commodity")

    shipments = Shipment.objects.using(db_alias).filter(models.Q(reference__gt=25))
    commodities = Commodity.objects.using(db_alias).filter(
        models.Q(description__gt=25) | models.Q(sku__gt=25) | models.Q(hs_code__gt=25)
    )
    parcels = Parcel.objects.using(db_alias).filter(
        models.Q(description__gt=35)
        | models.Q(content__gt=35)
        | models.Q(reference_number__gt=50)
    )
    addresses = Address.objects.using(db_alias).filter(
        models.Q(city__gt=30)
        | models.Q(person_name__gt=30)
        | models.Q(company_name__gt=30)
        | models.Q(phone_number__gt=20)
        | models.Q(federal_tax_id__gt=20)
        | models.Q(state_tax_id__gt=20)
        | models.Q(address_line1__gt=35)
        | models.Q(address_line2__gt=35)
    )

    for shipment in shipments:
        if shipment.reference:
            shipment.reference_temp = shipment.reference[:35]

        shipment.save()

    for parcel in parcels:
        if parcel.content:
            parcel.content_temp = parcel.content[:35]

        if parcel.description:
            parcel.description_temp = parcel.description[:35]

        if parcel.reference_number:
            parcel.reference_number_temp = parcel.reference_number[:50]

        parcel.save()

    for commodity in commodities:
        if commodity.description:
            commodity.description_temp = commodity.description[:25]

        if commodity.sku:
            commodity.sku_temp = commodity.sku[:25]

        if commodity.hs_code:
            commodity.hs_code_temp = commodity.hs_code[:25]

        commodity.save()

    for address in addresses:
        if address.city:
            address.city_temp = address.city[:30]
        if address.federal_tax_id:
            address.federal_tax_id_temp = address.federal_tax_id[:20]
        if address.state_tax_id:
            address.state_tax_id_temp = address.state_tax_id[:20]
        if address.person_name:
            address.person_name_temp = address.person_name[:30]
        if address.company_name:
            address.company_name_temp = address.company_name[:30]
        if address.address_line1:
            address.address_line1_temp = address.address_line1[:35]
        if address.address_line2:
            address.address_line2_temp = address.address_line2[:35]

        address.save()


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0043_customs_duty_billing_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="address_line1_temp",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="address",
            name="address_line2_temp",
            field=models.CharField(
                blank=True, db_index=True, max_length=100, null=True
            ),
        ),
        migrations.AddField(
            model_name="address",
            name="city_temp",
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="address",
            name="company_name_temp",
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="address",
            name="federal_tax_id_temp",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="address",
            name="person_name_temp",
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="address",
            name="phone_number_temp",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="address",
            name="state_tax_id_temp",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="commodity",
            name="description_temp",
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name="commodity",
            name="hs_code_temp",
            field=models.CharField(blank=True, db_index=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name="commodity",
            name="sku_temp",
            field=models.CharField(blank=True, db_index=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name="parcel",
            name="content_temp",
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name="parcel",
            name="description_temp",
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name="parcel",
            name="reference_number_temp",
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="shipment",
            name="reference_temp",
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        # Copy fields
        migrations.RunPython(forwards_func, reverse_func),
        # Remove fields
        migrations.RemoveField(
            model_name="address",
            name="address_line1",
        ),
        migrations.RemoveField(
            model_name="address",
            name="address_line2",
        ),
        migrations.RemoveField(
            model_name="address",
            name="city",
        ),
        migrations.RemoveField(
            model_name="address",
            name="company_name",
        ),
        migrations.RemoveField(
            model_name="address",
            name="federal_tax_id",
        ),
        migrations.RemoveField(
            model_name="address",
            name="person_name",
        ),
        migrations.RemoveField(
            model_name="address",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="address",
            name="state_tax_id",
        ),
        migrations.RemoveField(
            model_name="commodity",
            name="description",
        ),
        migrations.RemoveField(
            model_name="commodity",
            name="hs_code",
        ),
        migrations.RemoveField(
            model_name="commodity",
            name="sku",
        ),
        migrations.RemoveField(
            model_name="parcel",
            name="content",
        ),
        migrations.RemoveField(
            model_name="parcel",
            name="description",
        ),
        migrations.RemoveField(
            model_name="parcel",
            name="reference_number",
        ),
        migrations.RemoveField(
            model_name="shipment",
            name="reference",
        ),
        # Rename fields
        migrations.RenameField(
            model_name="address",
            old_name="address_line1_temp",
            new_name="address_line1",
        ),
        migrations.RenameField(
            model_name="address",
            old_name="address_line2_temp",
            new_name="address_line2",
        ),
        migrations.RenameField(
            model_name="address",
            old_name="city_temp",
            new_name="city",
        ),
        migrations.RenameField(
            model_name="address",
            old_name="company_name_temp",
            new_name="company_name",
        ),
        migrations.RenameField(
            model_name="address",
            old_name="federal_tax_id_temp",
            new_name="federal_tax_id",
        ),
        migrations.RenameField(
            model_name="address",
            old_name="person_name_temp",
            new_name="person_name",
        ),
        migrations.RenameField(
            model_name="address",
            old_name="phone_number_temp",
            new_name="phone_number",
        ),
        migrations.RenameField(
            model_name="address",
            old_name="state_tax_id_temp",
            new_name="state_tax_id",
        ),
        migrations.RenameField(
            model_name="commodity",
            old_name="description_temp",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="commodity",
            old_name="hs_code_temp",
            new_name="hs_code",
        ),
        migrations.RenameField(
            model_name="commodity",
            old_name="sku_temp",
            new_name="sku",
        ),
        migrations.RenameField(
            model_name="parcel",
            old_name="content_temp",
            new_name="content",
        ),
        migrations.RenameField(
            model_name="parcel",
            old_name="description_temp",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="parcel",
            old_name="reference_number_temp",
            new_name="reference_number",
        ),
        migrations.RenameField(
            model_name="shipment",
            old_name="reference_temp",
            new_name="reference",
        ),
    ]
