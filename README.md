# The problem
Python projects have many files of source code.

Every source code file imports another source code files.

Sooner or later, you'll get following import after import
without finding a "pure" file without dependencies.

# The solution

Use a dependency tree!

```
$ deptree [PATH]
```

# Examples
Let's clone a real project:

```
$ git clone https://github.com/yaml/pyyaml.git
```

And create a dependency tree:

```
$ cd pyyaml/lib3
$ deptree yaml
    # We should start reading this files since they have no dependencies
    yaml/events.py
    yaml/tokens.py
    yaml/error.py
    yaml/nodes.py
    # Then read this files which depends on the previous files
    yaml/emitter.py
        error
        events
    yaml/scanner.py
        error
        tokens
    yaml/composer.py
        error
        events
        nodes
    yaml/resolver.py
        error
        nodes
        re
    yaml/serializer.py
        error
        events
        nodes
    yaml/reader.py
        codecs
        error
        re
    # And so on
    yaml/dumper.py
        emitter
        representer
        resolver
        serializer
    yaml/parser.py
        error
        events
        scanner
        tokens
```

# How to install

Just clone this repository and build from scratch:

```
$ git clone https://github.com/kamadorueda/dependency-tree.git
$ cd dependency-tree
$ python3 -m pip install --user .
```
