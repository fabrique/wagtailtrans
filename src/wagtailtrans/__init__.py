default_app_config = 'wagtailtrans.apps.WagtailTransConfig'

VERSION = (2, 2, 1, 'wagtail2.11-5', '-')


def get_version():
    """Return normalised version string."""
    version = '%s.%s' % (VERSION[0], VERSION[1])
    # Append 3rd digit if > 0
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])

    if VERSION[3] != 'final' and len(VERSION) == 5 and VERSION[4]:
        version = '%s%s%s' % (version, VERSION[4], VERSION[3])
    elif VERSION[3] != 'final':
        version = '%s.%s' % (version, VERSION[3])
    return version
