import importlib


def ontology_class(cls):
    class NewCls(object):
        def __init__(self, *args, **kwargs):
            self.oInstance = cls(*args, **kwargs)

            package_name = ".".join([object.__module__, object.__name__])
            module = importlib.import_module(package_name)

            # inject the base_uri, version and complete_uri from the GCF ontology package
            self.base_uri = module.base_uri
            self.version = module.version
            self.complete_uri = module.complete_uri

        def __getattribute__(self, s):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and
            the attribute is an instance method then `time_this` is applied.
            """
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__):  # it is an instance method
                return time_this(
                    x
                )  # this is equivalent of just decorating the method with time_this
            else:
                return x

    return NewCls
