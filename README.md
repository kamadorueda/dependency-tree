# The problem
Python projects have many files of source code.
Every source code file imports another source code files.
Sooner or later, you'll get following import after import
without finding a "pure" file without dependencies
and start right there understanding the project.

# The solution

Just clone the repository and install it:
$ git clone https://github.com/kamadorueda/dependency-tree.git
$ cd dependency-tree
$ python3 -m pip install --user .

Now run it against a project:
$ deptree [PATH]

# Examples
Let's clone a real project:
$ git clone https://github.com/yaml/pyyaml.git

And create a dependency tree:
$ deptree pyyaml/lib3/yaml
    # We should start reading this files since they have no dependencies
    pyyaml/lib3/yaml/events.py
    pyyaml/lib3/yaml/tokens.py
    pyyaml/lib3/yaml/error.py
    pyyaml/lib3/yaml/nodes.py
    # Then read this files which depends on the previous files
    pyyaml/lib3/yaml/emitter.py
        error
        events
    pyyaml/lib3/yaml/scanner.py
        error
        tokens
    pyyaml/lib3/yaml/composer.py
        error
        events
        nodes
    pyyaml/lib3/yaml/resolver.py
        error
        nodes
        re
    pyyaml/lib3/yaml/serializer.py
        error
        events
        nodes
    pyyaml/lib3/yaml/reader.py
        codecs
        error
        re
    # And so on
    pyyaml/lib3/yaml/dumper.py
        emitter
        representer
        resolver
        serializer
    pyyaml/lib3/yaml/parser.py
        error
        events
        scanner
        tokens
    pyyaml/lib3/yaml/cyaml.py
        _yaml
        constructor
        representer
        resolver
        serializer
    pyyaml/lib3/yaml/loader.py
        composer
        constructor
        parser
        reader
        resolver
        scanner
    pyyaml/lib3/yaml/__init__.py
        cyaml
        dumper
        error
        events
        io
        loader
        nodes
        tokens
    pyyaml/lib3/yaml/representer.py
        base64
        collections
        copyreg
        datetime
        error
        nodes
        sys
        types
    pyyaml/lib3/yaml/constructor.py
        base64
        binascii
        collections
        datetime
        error
        nodes
        re
        sys
        types
