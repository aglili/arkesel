from setuptools import setup,find_packages



setup(
    name="arkesel",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        'certifi==2023.7.22',
        'charset-normalizer==3.2.0',
        'docutils==0.20.1',
        'idna==3.4',
        'importlib-metadata==6.8.0',
        'jaraco.classes==3.3.0',
        'keyring==24.2.0',
        'markdown-it-py==3.0.0',
        'mdurl==0.1.2',
        'more-itertools==10.1.0',
        'nh3==0.2.14',
        'pkginfo==1.9.6',
        'Pygments==2.16.1',
        'pywin32-ctypes==0.2.2',
        'readme-renderer==42.0',
        'requests==2.31.0',
        'requests-toolbelt==1.0.0',
        'rfc3986==2.0.0',
        'rich==13.5.3',
        'twine==4.0.2',
        'urllib3==2.0.4',
        'zipp==3.16.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    # meta data
    author="Aglili Selorm Cecil",
    author_email="cecilselorm34@gmail.com",
    description= "Un-Official API-Wrapper for the Arkesel API",
    url="https://github.com/aglili/arkesel-py",
    license="MIT"
)