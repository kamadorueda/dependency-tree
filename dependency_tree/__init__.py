"""Dependency Tree."""

import os
import ast
import argparse


def get_ast(file_path):
    """Return an AST object from a python file."""
    with open(file_path, "r") as file:
        file_ast = ast.parse(file.read())
    return file_ast


def get_python_files(path: str):
    """Return a list of paths for every python file in path."""
    python_files = []
    for root, _, files in os.walk(path, followlinks=True):
        for file_name in files:
            if os.path.splitext(file_name)[1] == ".py":
                file_path = os.path.relpath(
                    os.path.join(root, file_name))
                python_files.append(file_path)
    return python_files


def get_dependency_tree(path: str):
    """Parse the path to create a data structure with the dependencies."""
    dependencies = {}
    for file_path in get_python_files(path):
        file_ast = get_ast(file_path)
        dependencies[file_path] = []
        for node in ast.walk(file_ast):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    dependencies[file_path].append(alias.name)
            if isinstance(node, ast.ImportFrom):
                _from = node.module
                if _from:
                    dependencies[file_path].append(_from)
                else:
                    for alias in node.names:
                        dependencies[file_path].append(alias.name)
                # _level = node.level
    return dependencies


def print_dependency_tree(dep_tree):
    """Pretty print the dependency tree to stdout."""
    get_count = lambda x: len(dep_tree[x])
    sorted_dep_tree = {
        k: dep_tree[k]
        for k in sorted(dep_tree, key=get_count)
    }
    for file_path, dependencies in sorted_dep_tree.items():
        print(file_path)
        for dependency in sorted(dependencies):
            print(f"    {dependency}")


def main():
    """Usual entry point."""
    parser = argparse.ArgumentParser(
        description="Create a dependency tree for your python project.")
    parser.add_argument(
        "path",
        help="Path to the project.")
    args = parser.parse_args()
    dependency_tree = get_dependency_tree(args.path)
    print_dependency_tree(dependency_tree)


if __name__ == "__main__":
    main()
