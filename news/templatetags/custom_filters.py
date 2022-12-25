from django import template

register = template.Library()
@register.filter(name='Censor')
def censor(value, arg):
	if isinstance(value,str):
		arg = str(arg)
		return value.replace(arg, '[скрыто]')