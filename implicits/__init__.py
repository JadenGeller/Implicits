import inspect
import platform

def _default_args(func):
    if platform.python_version().startswith("2."):
        return inspect.getargspec(func).defaults
    else:
        return [
            name 
            for name, parameter in inspect.signature(func).parameters.items()
            if parameter.default is not inspect.Parameter.empty
        ]

def implicit(*implicit_arg_names):
    def decorator(func):
        defaults = _default_args(func)
        def wrapper(*args, **kwargs):
            caller_locals = inspect.currentframe().f_back.f_locals
            for name in implicit_arg_names:
                if name in kwargs:
                    continue
                elif name in caller_locals:
                    kwargs[name] = caller_locals[name]
                elif name not in defaults:
                    raise NameError("implicit name '{}' is not defined in caller's locals".format(name))
            return func(*args, **kwargs)
        return wrapper
    return decorator
