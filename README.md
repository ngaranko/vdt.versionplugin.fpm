vdt.versionplugin.fpm
=====================

Plugin for https://github.com/devopsconsulting/vdt.version

This plugin uses FPM. See also http://gofedora.wordpress.com/2012/04/19/easy-package-management-with-fpm/

FPM should be install as a gem using rubygems : 

```shell
gem install fpm
```

After that you can use this plugin the following way : 

```
version --plugin fpm -v --name <name of the package> -t <package type> -a <architecture> --prefix <prefix directory> --maintainer <maintainer> <files or directories to package>
```

For example, if you are using vdt.buildout :

```shell
cd src/ames.frontend
../../bin/version --plugin fpm -v --name ames.frontend -t deb -a all --prefix /usr/local/share/ames.frontend --maintainer martijn@kamaramusic.nl *
```

Extra arguments are passed trough FPM. Within jenkins you should use the -B flag to add the jenkins build version to the package.

By default this plugin is trying to checkout tag prvided by 'vdt.version' however it's not always required.
In order to avoid this pass extra parameter `--no-checkout` to plugin.

