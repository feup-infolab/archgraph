import argparse


def parse():
    parser = argparse.ArgumentParser(description="Starts the archgraph server.")
    parser.add_argument("--mongodb", nargs="?", help="Address of the mongodb server")
    parser.add_argument("--neo4j", nargs="?", help="Address of the neo4j server")
    parser.add_argument("--host", nargs="?", help="Address of the neo4j server")

    args = parser.parse_args()

    return args


class ArgParser:
    pass
