# -*- coding: utf-8 -*-

'''
Default 51Degrees Mobile Detector settings. Override these using the
FIFTYONE_DEGREES_MOBILE_DETECTOR_SETTINGS environment variable. Both file
paths (e.g. '/etc/51degrees-mobile-detector.settings.py') and module
names (e.g. 'myproject.fiftyone_degrees_mobile_settings') are allowed.
If not specified, defaults to '51degrees-mobile-detector.settings.py'
in the current working directory.

Note that when using the mobile detector in a Django project, settings
can also be specified using the FIFTYONE_DEGREES_MOBILE_DETECTOR_SETTINGS
variable in the Django settings file.

:copyright: (c) 2013 by 51Degrees.mobi, see README.rst for more details.
:license: MPL2, see LICENSE.txt for more details.
'''

from __future__ import absolute_import

###############################################################################
## GENERAL SETTINGS.
###############################################################################

# Sets the preferred mobile device detection method. Available options are:
#
#   - 'lite-pattern-wrapper': Requires '51degrees-mobile-detector-lite-pattern-wrapper' package.
#   - 'premium-pattern-wrapper': Requires '51degrees-mobile-detector-premium-pattern-wrapper' package.
#   - 'trie-wrapper': Requires '51degrees-mobile-detector-trie-wrapper' package.
#
DETECTION_METHOD = 'lite-pattern-wrapper'

# List of case-sensitive property names to be fetched on every device detection. Leave empty to
# fetch all available properties.
PROPERTIES = ()

# Your 51Degrees license key. This is required if you want to set up the automatic
# 51degrees-mobile-detector-premium-pattern-wrapper package updates.
LICENSE = ''

###############################################################################
## TRIE DETECTOR (C WRAPPER) SETTINGS.
###############################################################################

# Location of the database file. If not specified, the trie-based detection
# method will not be available. Download the latest 51Degrees.mobi-Lite-*.trie.zip
# file from http://sourceforge.net/projects/fiftyone-c/files/.
TRIE_WRAPPER_DATABASE = '/path/to/51Degrees.mobi-Lite.trie.dat'

###############################################################################
## USAGE SHARER SETTINGS.
###############################################################################

# Indicates if usage data should be shared with 51Degrees.mobi. We recommended
# leaving this value unchanged to ensure we're improving the performance and
# accuracy of the solution.
USAGE_SHARER_ENABLED = True

# The detail that should be provided relating to new devices.
# Modification not required for most users.
USAGE_SHARER_MAXIMUM_DETAIL = True

# URL to send new device data to.
# Modification not required for most users.
USAGE_SHARER_SUBMISSION_URL = 'http://devices.51degrees.mobi/new.ashx'

# Data submission timeout (seconds).
USAGE_SHARER_SUBMISSION_TIMEOUT = 10

# Minimum queue length to launch data submission.
USAGE_SHARER_MINIMUM_QUEUE_LENGTH = 50

# Used to detect local devices.
# Modification not required for most users.
USAGE_SHARER_LOCAL_ADDRESSES = (
    '127.0.0.1',
    '0:0:0:0:0:0:0:1',
)

# The content of fields in this list should not be included in the
# request information sent to 51Degrees.
# Modification not required for most users.
USAGE_SHARER_IGNORED_HEADER_FIELD_VALUES = (
    'Referer',
    'cookie',
    'AspFilterSessionId',
    'Akamai-Origin-Hop',
    'Cache-Control',
    'Cneonction',
    'Connection',
    'Content-Filter-Helper',
    'Content-Length',
    'Cookie',
    'Cookie2',
    'Date',
    'Etag',
    'If-Last-Modified',
    'If-Match',
    'If-Modified-Since',
    'If-None-Match',
    'If-Range',
    'If-Unmodified-Since',
    'IMof-dified-Since',
    'INof-ne-Match',
    'Keep-Alive',
    'Max-Forwards',
    'mmd5',
    'nnCoection',
    'Origin',
    'ORIGINAL-REQUEST',
    'Original-Url',
    'Pragma',
    'Proxy-Connection',
    'Range',
    'Referrer',
    'Script-Url',
    'Unless-Modified-Since',
    'URL',
    'UrlID',
    'URLSCAN-ORIGINAL-URL',
    'UVISS-Referer',
    'X-ARR-LOG-ID',
    'X-Cachebuster',
    'X-Discard',
    'X-dotDefender-first-line',
    'X-DRUTT-REQUEST-ID',
    'X-Initial-Url',
    'X-Original-URL',
    'X-PageView',
    'X-REQUEST-URI',
    'X-REWRITE-URL',
    'x-tag',
    'x-up-subno',
    'X-Varnish',
)