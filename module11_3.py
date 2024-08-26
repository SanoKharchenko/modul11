import inspect


def introspection_info(obj):
    total = {}
    total['tipe'] = type(obj).__name__
    total['attributes'] = [i for i in dir(obj) if not callable(getattr(obj, i))]
    total['metod'] = [i for i in dir(obj) if callable(getattr(obj, i))]
    total['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None
    return total


if __name__ == "__main__":

    number_info = introspection_info(42)
    print(number_info)