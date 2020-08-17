# coding=utf-8

"""
Created by Jayvee on 2020-01-13.
https://github.com/JayveeHe
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FaissToolBox",
    version="0.0.1",
    author="Jayvee He",
    author_email="jayveehe@gmail.com",
    description="A Toolbox for Vector Similarity Search based on Faiss Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JayveeHe/FaissToolBox",
    packages=['faisstoolbox','faisstoolbox.utils'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
        'faiss-cpu',
    ]
)
