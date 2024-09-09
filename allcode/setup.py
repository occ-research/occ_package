from setuptools import setup
from setuptools import find_packages

setup(
    name='occlab',
    version='0.0.2',
    install_requires=[
        'requests',
        'importlib-metadata; python_version<"3.10"',
    ],
)

setup(
    setup_requires=['wheel']
)

setup(
    packages=find_packages(
        where='src',
        include=['wocemaps','spmap'],  # alternatively: `exclude=['additional*']`
    ),
    package_dir={"": "src"}
)
