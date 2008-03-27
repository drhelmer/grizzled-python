# $Id$

"""
Provides some base exception classes.
"""

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class ExceptionWithMessage(Exception):
    """
    Useful base class for exceptions that have a single exception message
    argument. Among other things, this method provides a reasonable default
    C{__str__()} method.

    Usage::

        from grizzled.exception import ExceptionWithMessage

        class MyException(ExceptionWithMessage):
            def __init__(self, msg):
                ExceptionWithMessage.__init__(self, msg)
    """
    def __init__(self, errorMessage):
        """
        Create a new exception.

        @type errorMessage:  string
        @param errorMessage: the error message
        """
        self.__message = errorMessage

    @property
    def message(self):
        """
        The message stored with this object.
        """
        return self.__message

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.__message)