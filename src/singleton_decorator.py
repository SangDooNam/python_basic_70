def singleton(class_):
    # Complete this function
    instance = {} 
    def wrapped(*args, **kwargs):
        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)
        return instance[class_]
    return wrapped
