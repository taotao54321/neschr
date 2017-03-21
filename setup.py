# -*- coding: utf-8 -*-


from setuptools import setup


setup(
    name="neschr",
    version="0.1.0",

    description="NES CHR parser",
    long_description=open("README.rst").read(),
    license="GPLv3",

    url="https://github.com/taotao54321/neschr",
    author="TaoTao",
    author_email="taotao54321@gmail.com",

    classifiers=(
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ),

    keywords="NES",

    packages=("neschr",),

    install_requires=("pillow",),
)
