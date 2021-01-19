from CSVmaker.models import NewSchema

from django import forms
from django.core.exceptions import ValidationError  # noqa
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import Form, fields


class NewSchemaCreateForm(forms.ModelForm):
    class Meta:
        model = NewSchema
        fields = ['name', 'column_separ', 'str_char', 'column_name', 'column_type', 'column_name1', 'column_type1',
                  'column_name2', 'column_type2', 'column_name3', 'column_type3', 'column_name4', 'column_type4']


class SchemaEditForm(NewSchemaCreateForm):
    class Meta(NewSchemaCreateForm.Meta):
        fields = ['name', 'column_separ', 'str_char', 'column_name', 'column_type', 'column_name1', 'column_type1',
                  'column_name2', 'column_type2', 'column_name3', 'column_type3', 'column_name4', 'column_type4']


class NumberRow(Form):
    row_number = fields.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000000000)])
