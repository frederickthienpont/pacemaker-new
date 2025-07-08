# setup.py
from setuptools import setup, find_packages

setup(pip install pyinstaller
     )
    name='utils_project',
    version='1.0',
    packages=find_packages(1),
    install_requires=[
        # Voeg hier extra dependencies toe als je die hebt
    ],
    entry_points={
        'console_scripts': [
            'utils=utils:main',  # Dit zou het entrypoint voor je project zijn
        ],
    },
)
