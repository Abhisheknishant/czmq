################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
from .utils import *
from . import native
from . import destructors
libczmq = native.lib
libczmq_destructors = destructors.lib
ffi = native.ffi

class Zargs(object):
    """
    Platform independent command line argument parsing helpers

There are two kind of elements provided by this class
foo --named-parameter --parameter with_value positional arguments -a gain-parameter
zargs keeps poision only for arguments, parameters are to be accessed like hash.

It DOES:
* provide easy to use CLASS compatible API for accessing argv
* is platform independent
* provide getopt_long style -- argument, which delimits parameters from arguments
* makes parameters positon independent

It does NOT
* change argv
* provide a "declarative" way to define command line interface

In future it SHALL
* hide several formats of command line to one (-Idir, --include=dir,
  --include dir are the same from API pov)
    """

    def __init__(self, argc, argv):
        """
        Create a new zargs from command line arguments.
        """
        p = libczmq.zargs_new(self._p, argc, to_bytes(argv))
        if p == ffi.NULL:
            raise MemoryError("Could not allocate person")

        # ffi.gc returns a copy of the cdata object which will have the
        # destructor called when the Python object is GC'd:
        # https://cffi.readthedocs.org/en/latest/using.html#ffi-interface
        self._p = ffi.gc(p, libczmq_destructors.zargs_destroy_py)

    def progname(self):
        """
        Return program name (argv[0])
        """
        return libczmq.zargs_progname(self._p)

    def arguments(self):
        """
        Return number of positional arguments
        """
        return libczmq.zargs_arguments(self._p)

    def first(self):
        """
        Return first positional argument or NULL
        """
        return libczmq.zargs_first(self._p)

    def next(self):
        """
        Return next positional argument or NULL
        """
        return libczmq.zargs_next(self._p)

    def param_first(self):
        """
        Return first named parameter value, or NULL if there are no named
        parameters, or value for which zargs_param_empty (arg) returns true.
        """
        return libczmq.zargs_param_first(self._p)

    def param_next(self):
        """
        Return next named parameter value, or NULL if there are no named
        parameters, or value for which zargs_param_empty (arg) returns true.
        """
        return libczmq.zargs_param_next(self._p)

    def param_name(self):
        """
        Return current parameter name, or NULL if there are no named
        parameters.
        """
        return libczmq.zargs_param_name(self._p)

    def param_lookup(self, keys):
        """
        Return value of named parameter, NULL if no given parameter has
        been specified, or special value for wich zargs_param_empty ()
        returns true.
        """
        return libczmq.zargs_param_lookup(self._p, to_bytes(keys))

    def param_lookupx(self, keys, ):
        """
        Return value of named parameter(s), NULL if no given parameter has
        been specified, or special value for wich zargs_param_empty ()
        returns true.
        """
        return libczmq.zargs_param_lookupx(self._p, to_bytes(keys), )

    def has_help(self):
        """
        Returns true if there are --help -h arguments
        """
        return libczmq.zargs_has_help(self._p)

    def param_empty(arg):
        """
        Returns true if parameter did not have a value
        """
        return libczmq.zargs_param_empty(to_bytes(arg))

    def print_py(self):
        """
        Print an instance of zargs.
        """
        return libczmq.zargs_print(self._p)

    def test(verbose):
        """
        Self test of this class.
        """
        return libczmq.zargs_test(verbose)

################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################