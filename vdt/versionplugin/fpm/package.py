import logging
import subprocess


log = logging.getLogger('vdt.versionplugin.fpm.package')


def build_package(version):
    """
    Build package with fpm.
    """
    log.debug("Building version {0} with fpm.".format(version))

    if "--no-checkout" in version.extra_args:
        # No tag checkout needed.
        args = version.extra_args
        del(args[args.index("--no-checkout")])
        call_fpm(version, args)
    else:
        # Fallback to old functionality
        with version.checkout_tag:
            call_fpm(version)

def call_fpm(version, extra_args=None):
    """
    Calls `fpm` with conditional extra arguments
    """
    cmd = ['fpm', '-s', 'dir', '--version=%s' % version]
    cmd.extend(extra_args or version.extra_args)
    log.debug("Running command '%s'" % " ".join(cmd))
    subprocess.check_call(cmd)

def set_package_version(version):
    """
    If there need to be modifications to source files before a
    package can be built (changelog, version written somewhere etc.)
    that code should go here
    """
    log.debug("set_package_version is not implemented for fpm")
