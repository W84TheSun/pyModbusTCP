from pyModbusTCP import constants
from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

requires = [
    "win_inet_pton=>1.0.1",
]

setup(
    name="pyModbusTCP",
    version=constants.VERSION,
    description="A simple Modbus/TCP library for Python",
    long_description=readme,
    author="Loic Lefebvre",
    author_email="loic.celine@free.fr",
    license = "MIT",
    url="https://github.com/sourceperl/pyModbusTCP",
    packages=["pyModbusTCP"],
    platforms="any",
    install_requires=requires,
    )
