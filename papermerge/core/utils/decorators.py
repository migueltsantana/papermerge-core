from papermerge.core.config import get_settings


config = get_settings()


def if_redis_present(orig_func):
    """Skip decorated function when `config.papermerge__redis__url` is None"""

    def inner(*args, **kwargs):
        if config.papermerge__redis__url is not None:
            orig_func(*args, **kwargs)

    return inner


def docstring_parameter(**kwargs):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(**kwargs)
        return obj

    return dec
