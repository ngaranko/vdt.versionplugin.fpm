import logging
import subprocess


log = logging.getLogger('vdt.versionplugin.fpm.package')


def set_version(version):
    """
    """
    return version

def build_package(version):
    """
    Build package with fpm.
    """
    log.debug("Building version {0} with fpm.".format(version))
    #with version.checkout_tag:
    cmd = ['fpm', '-s', 'dir', '--version=%s' % version] + version.extra_args
    log.debug("Running command %s" % " ".join(cmd))
    subprocess.check_call(cmd)


def set_package_version(version):
    """
    If there need to be modifications to source files before a
    package can be built (changelog, version written somewhere etc.)
    that code should go here
    """
    log.debug("set_package_version is not implemented for fpm")

