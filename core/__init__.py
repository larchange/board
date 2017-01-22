from functools import singledispatch


@singledispatch
def to_html(obj):
    try:
        return obj.render_html()
    except:
        return str(obj)


@singledispatch
def to_js(obj):
    try:
        return obj.render_js()
    except:
        return ""

