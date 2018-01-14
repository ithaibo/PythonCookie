class Error(Exception):
    """Base class for exception in this modules"""
    pass

try:
    raise Error
except Error:
    print "an error caused."