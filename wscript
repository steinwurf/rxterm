#!  /usr/bin/env python
# encoding: utf-8

APPNAME = 'rxterm'
VERSION = '1.0.0'


def build(bld):

    bld.env.append_unique('DEFINES_STEINWURF_VERSION',
                          'STEINWURF_RXTERM_VERSION="{}"'.format(VERSION))

    # Path to the rxterm repo
    rxterm_path = bld.dependency_node("rxterm-source")

    bld(includes=rxterm_path,
        export_includes=rxterm_path.find_dir('include').abspath(),
        name='rxterm')

    if bld.is_toplevel():

        # Build demo
        bld(features='cxx cxxprogram',
            source=rxterm_path.ant_glob('apps/*.cpp'),
            target='demo',
            use=['rxterm'])
