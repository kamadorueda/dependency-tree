"""Package setup file."""

import setuptools

setuptools.setup(
    name="dependency_tree",
    version="0.0",
    description="",

    author="Kevin Amado",
    url="https://github.com/kamadorueda/dependency-tree",

    py_modules=[
    ],

    install_requires=[
    ],

    entry_points="""
        [console_scripts]
        deptree=dependency_tree:main
    """,

    packages=[
        "dependency_tree"
    ],
)
