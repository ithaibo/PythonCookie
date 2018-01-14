class Error(Exception):
    """Base class for exception in this modules"""
    pass

    def showCaused():
        return "something error happen"

try:
    raise Error
except Error:
    print "an error caused."