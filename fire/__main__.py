#!/usr/bin/env python
"""Run fire on the given module or file

Usage: fire [module | file] [fire-style arguments to desired python object]

Example:

$ fire random Random gauss 3 4
5.056813212816271

Documentation on fire:
 https://github.com/google/python-fire/blob/master/doc/guide.md

Discussion: https://github.com/google/python-fire/issues/29
"""

import fire
import imp
import sys

if __name__ == '__main__':
    module_or_file = sys.argv[1]

    try:
        fileobj = None
        (fileobj, pathname, description) = imp.find_module(module_or_file)
        module = imp.load_module('module', fileobj, pathname, description)
        sys.argv = sys.argv[1:]

    except ImportError:
        try:
            module = imp.load_source('module', module_or_file)
            sys.argv = sys.argv[1:]
        except (ImportError, EnvironmentError):
            # or be specific about FileNotFoundError and ? in python2?
            print("No such module or file: %s" % module_or_file)
            print("Usage: fire [module | file] [fire-style arguments to desired python object]")
            sys.exit(1)
        
    finally:
        if fileobj:
            fileobj.close()
        
    from module import *

    fire.Fire()
