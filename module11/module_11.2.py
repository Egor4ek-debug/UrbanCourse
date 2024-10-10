import inspect


def introspection_info(obj):
    obj_type = type(obj)

    obj_module = obj.__module__ if hasattr(obj, '__module__') else '__main__'

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    other_properties = {}
    if inspect.isfunction(obj):
        other_properties['signature'] = str(inspect.signature(obj))
    elif inspect.ismodule(obj):
        other_properties['file'] = getattr(obj, '__file__', 'Not Available')
    elif isinstance(obj, (list, dict, set, tuple)):
        other_properties['length'] = len(obj)

    result = {
        'type': obj_type,
        'module': obj_module,
        'attributes': attributes,
        'methods': methods,
        'other_properties': other_properties
    }

    return result


number_info = introspection_info(42)
print(number_info)
