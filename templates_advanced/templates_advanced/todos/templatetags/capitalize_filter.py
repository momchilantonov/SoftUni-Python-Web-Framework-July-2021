from django import template


register = template.Library()


@register.filter(name='capitalize')
def capitalize(value, chars_count):
    return value[:chars_count].upper() + value[chars_count:]
    # return value.capitalize()