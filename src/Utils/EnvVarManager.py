import argparse


def parse():
    import os

    args = dict()
    if "NEO4J_HOST" in os.environ:
        args["NEO4J_HOST"] = os.environ["NEO4J_HOST"]

    if "NEO4J_PORT" in os.environ:
        args["NEO4J_PORT"] = os.environ["NEO4J_PORT"]

    if "MONGODB_HOST" in os.environ:
        args["MONGODB_HOST"] = os.environ["MONGODB_HOST"]

    if "MONGODB_PORT" in os.environ:
        args["MONGODB_PORT"] = os.environ["MONGODB_PORT"]

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
