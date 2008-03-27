# $Id$
#
# Nose program for testing grizzled.file classes/functions

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from grizzled.file import *
from cStringIO import StringIO
import os
import tempfile
import atexit

# ---------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Classes
# ---------------------------------------------------------------------------

class TestFilePackage(object):

    def testUnlinkQuietly(self):
        fd, path = tempfile.mkstemp()
        os.unlink(path)

        try:
            os.unlink(path)
            assert False, 'Expected an exception'
        except OSError:
            pass

        unlinkQuietly(path)

    def testRecursivelyRemove(self):
        path = tempfile.mkdtemp()
        print 'Created directory "%s"' % path

        # Create some files underneath

        touch([os.path.join(path, 'foo'),
               os.path.join(path, 'bar')])

        try:
            os.unlink(path)
            assert False, 'Expected an exception'
        except OSError:
            pass

        recursivelyRemove(path)

    def testTouch(self):
        path = tempfile.mkdtemp()
        atexit.register(recursivelyRemove, path)
        f = os.path.join(path, 'foo')
        assert not os.path.exists(f)
        touch(f)
        assert os.path.exists(f)
        