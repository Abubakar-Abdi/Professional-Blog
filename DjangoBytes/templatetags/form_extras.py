from django import template

register = template.Library()

@register.filter
def add_class(field, css_classes):
    classes = field.field.widget.attrs.get('class', '')
    classes += f' {css_classes}'
    return field.as_widget(attrs={'class': classes.strip()})
