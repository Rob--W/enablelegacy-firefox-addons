#!/usr/bin/env python2

import sys
install = sys.argv[1] == 'install'
omnija = sys.argv[2]

with open(omnija, 'rb') as f:
    data = f.read()

databackup = data


def setAppConstant(key, defaultValue, newValue):
    global data
    key = b' %s:\n' % key
    i = data.find(key)
    assert i != -1, b'Must find AppConstants.%s' % key
    i += len(key)

    # Find end of next line
    j = data.find(b'\n', i)
    assert i != -1, b'Must have a full line after AppConstants.%s key' % key
    line = data[i:j]
    assert b'AppConstants.jsm"' in line, b'Must be a comment: "%s"' % line
    i = j + 1  # 1 = len(b'\n')

    # Find the interesting line
    def makeLine(val): return b'  %s,' % val
    expectedLine = makeLine(defaultValue)
    j = data.find(b'\n', i)
    assert j != -1, b'Must have a line after AppConstants.%s' % key
    line = data[i:j]
    assert line == expectedLine, \
        b'AppConstants.%s: "%s" == "%s"' % (key, expectedLine, line)
    data = data[:i] + makeLine(newValue) + data[j:]


if install:
    setAppConstant(b'MOZ_REQUIRE_SIGNING', b'true', b'!!!1')
    setAppConstant(b'MOZ_ALLOW_LEGACY_EXTENSIONS', b'false', b'!!!!1')
else:
    setAppConstant(b'MOZ_REQUIRE_SIGNING', b'!!!1', b'true')
    setAppConstant(b'MOZ_ALLOW_LEGACY_EXTENSIONS', b'!!!!1', b'false')


# Write only after all validation has passed.

with open('%s.bak' % omnija, 'wb') as f:
    f.write(databackup)

with open(omnija, 'wb') as f:
    f.write(data)
