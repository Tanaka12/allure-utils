from setuptools import setup
import re

VERSIONFILE = "./_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

print(f"========> Current version is {verstr}")

setup(name='allure_utils',
      version=verstr,
      description='Allure utils',
      url='https://github.com/Tanaka12/allure-utils',
      author='Jose Peiro',
      packages=['allure_utils'],
      classifiers=[
          "Topic :: Allure :: Utils",
          "Programming Language :: Python :: 3",
          "License :: Free"],
      install_requires=[],
      tests_require=['pytest==8.2.2',
                     'pytest-mock==3.14.0'],
      zip_safe=False
)
