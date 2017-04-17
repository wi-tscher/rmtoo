#!/usr/bin/env python

from distutils.core import setup
import os
import sys

package = 'rmtoo'
version = '23'

add_data = []
for dadi in ['rmtoo/tests', 'rmtoo/collection']:
    for (path, dirs, files) in os.walk(dadi):
        add_data.append((
            'share/pyshared/' + path,
            [path + '/' + filename for filename in files]))


def adjust(input, output):
    if os.path.exists(output):
        input_time = os.path.getmtime(input)
        output_time = os.path.getmtime(output)
        setup_time = os.path.getmtime('setup.py')
        if output_time > input_time and output_time > setup_time:
            return
        os.chmod(output, os.stat.S_IROTH | os.stat.S_IRGRP
                 | os.stat.S_IREAD | os.stat.S_IWRITE)
        os.remove(output)
    sys.stdout.write('adjusting %s -> %s\n' % (input, output))
    buffer = file(input).read()
    file(output, 'w').write(buffer.replace('@VERSION@', version))
    os.chmod(output, os.stat.S_IROTH | os.stat.S_IRGRP
                 | os.stat.S_IREAD | os.stat.S_IWRITE)


setup(name=package, version=version,
      description='Requirements Management Tool',
      author='Andreas Florath',
      author_email='rmtoo@florath.net',
      url='http://rmtoo.florath.net',
      packages=['rmtoo', 'rmtoo/lib',
                'rmtoo/inputs', 'rmtoo/tests', 'rmtoo/outputs',
                'rmtoo/lib/analytics',
                'rmtoo/lib/configuration',
                'rmtoo/lib/digraph',
                'rmtoo/lib/logging',
                'rmtoo/lib/main',
                'rmtoo/lib/storagebackend', 'rmtoo/lib/xmlutils/',
                'rmtoo/lib/storagebackend/txtfile',
                'rmtoo/lib/vcs',
                'rmtoo/lib/xmlutils',
                'rmtoo/collection', 'rmtoo/collection/constraints',
                'rmtoo/tests/lib', 'rmtoo/tests/RMTTest_Syntax',
                'rmtoo/tests/RMTTest_Unit',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Tag',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Digraph',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Core',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Core/testdata',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Core/testdata/modules01',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Core/testdata/modules02',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Core/testdata/modules03',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Core/testdata/modules04',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Core/testdata/modules05',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Core/testdata/modules06',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Core/testdata/modules07',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Core/testdata/modules08',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Topic',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Topic/testdata',
                'rmtoo/tests/RMTTest_Unit/RMTTest_Topic/testdata/topicset01',
                'rmtoo/tests/RMTTest_Output',

                # Blackbox Tests
                # are included with the 'add_data' statement.

                # contrib
                'rmtoo/contrib',
                # git-python
                'rmtoo/contrib/git',
                'rmtoo/contrib/git/repo',
                'rmtoo/contrib/git/refs',
                'rmtoo/contrib/git/index',
                'rmtoo/contrib/git/objects',
                'rmtoo/contrib/git/objects/submodule',
                # odf
                'rmtoo/contrib/odf',
                ],
      data_files=add_data,
      install_requires=['flake8', 'numpy', 'scipy', 'setuptools', 'nose',
                        "gitdb==0.5.4"],

      license="GPL V3",
      platforms="all",

      entry_points={
          'console_scripts': [
              "rmtoo = rmtoo.lib.RmtooMain:main",
              "rmtoo-configuration-convert = "
              "rmtoo.lib.main.ConfigurationConvert:main",
              "rmtoo-normalize-dependencies = "
              "rmtoo.lib.main.NormalizeDependencies:main",
              "rmtoo-pricing-graph = rmtoo.lib.main.PricingGraph:main",
          ]
      })
