from setuptools import find_packages, setup

setup(
    name='lektor-sparkle',
    version='0.1',
    packages=find_packages(),
    install_requires=['markupsafe', 'pytz'],
    entry_points={
        'lektor.plugins': [
            'sparkle = lektor_sparkle:SparklePlugin',
        ],
    },
)
