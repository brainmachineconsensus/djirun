from setuptools import setup, find_packages

setup(
    name='djirun',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'django',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'djirun = djirun.cli:main',
        ],
    },
    author='Fildouindé Ariel Shadrac OUEDRAOGO',
    author_email='arielshadrac@gmail.com',
    description="A CLI tool for fast and customizable Django project setup.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/brainmachineconsensus/djirun',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)