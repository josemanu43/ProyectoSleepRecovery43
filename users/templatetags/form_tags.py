# users/templatetags/form_tags.py
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Agrega una clase CSS a un campo de formulario de Django.
    Uso: {{ form.field|add_class:"clase-css" }}
    """
    return field.as_widget(attrs={"class": css_class})