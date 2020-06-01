import argparse


def parse():
    import os

    args = dict()
    if "NEO4J_CONNECTION_STRING" in os.environ:
        args["NEO4J_CONNECTION_STRING"] = os.environ["NEO4J_CONNECTION_STRING"]

    if "MONGODB_CONNECTION_STRING" in os.environ:
        args["MONGODB_CONNECTION_STRING"] = os.environ["MONGODB_CONNECTION_STRING"]

    if "CUSTOM_HOST_FOR_SERVER_BIND" in os.environ:
        args["CUSTOM_HOST_FOR_SERVER_BIND"] = os.environ["CUSTOM_HOST_FOR_SERVER_BIND"]

    if "CUSTOM_HOST_FOR_SERVER_BIND" in os.environ:
        args["CUSTOM_HOST_FOR_SERVER_BIND"] = os.environ["CUSTOM_HOST_FOR_SERVER_BIND"]

    return args


def get_from_env_or_return_default(var_name, default):
    args = parse()
    if var_name in args and args[var_name] != "":
        return args[var_name]
    else:
        return default


class ArgParser:
    pass
