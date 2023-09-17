from setuptools import setup,find_packages



setup(
    name="arkesel",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['requests'],

    # meta data
    author="Aglili Selorm Cecil",
    author_email="cecilselorm34@gmail.com",
    description= "Un-Official API-Wrapper for the Arkesel API",
    url="https://github.com/aglili/arkesel-py",
    license="MIT"
)