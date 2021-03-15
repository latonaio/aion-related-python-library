from setuptools import setup, find_packages

def _read_requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name = "aion",
    version = "0.0.1",
    author="sho ishii",
    author_email="sho.i@latonaio",
    packages = find_packages(),
    install_requires = _read_requires_from_file("requirements.txt")
)
