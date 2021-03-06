import setuptools
from distutils.core import setup
from distutils.extension import Extension
import numpy
import os

try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass = { }
ext_modules = [ ]

if use_cython:
    ext_modules += [
        Extension("correlade", [ "correlade/correlade.pyx" ]),
    ]
    cmdclass.update({ 'build_ext': build_ext })
else:
    ext_modules += [
        Extension("correlade", [ "correlade/correlade.c" ]),
    ]

print('Cython succeed: ', use_cython)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="correlade",
    version="0.2.12",
    author="Ian Coleman",
    author_email="colemai@tcd.ie",
    description="Correlation matrix of distance correlation",
    long_description="Pearson correlation only detects linear relationships\
    well, distance correlation is much more flexible. It's more computationally\
    intensive, so this package will randomly select 2000 rows if you feed it more\
    than that. There are other distance correlation computing packages around, \
    this one is just very quick and easy, like Pandas' corr() method ",
    long_description_content_type="text/markdown",
    url="https://github.com/colemai/correlade",
    packages=setuptools.find_packages(),
    cmdclass = cmdclass,
    ext_modules=ext_modules,    
    include_dirs=[numpy.get_include(),
                  os.path.join(numpy.get_include(), 'numpy')],
    zip_safe=False,
    setup_requires=[
          'cython',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
