from distutils.core import setup
import os

if os.path.exists("MANIFEST"):
    os.unlink("MANIFEST")

VERSION = ("12", "06", "0alpha", "0", )

setup(
    name='armstrong',
    version=".".join(VERSION),
    description="Armstrong is an open-source publishing system designed for news organizations that gives your team the technology edge it needs to report in a media-rich environment.",
    long_description=open("README.rst").read(),
    author='Bay Citizen & Texas Tribune',
    author_email='dev@armstrongcms.org',
    url='http://github.com/armstrong/armstrong/',
    packages=["armstrong", ],
    namespace_packages=["armstrong", ],
    install_requires=[
        "armstrong.cli>=1.2.0,<1.3",
        "armstrong.core.arm_access>=1.0.6,<1.1",
        "armstrong.core.arm_content>=1.3.1,<1.1",
        "armstrong.core.arm_layout>=1.1.1,<1.1",
        "armstrong.core.arm_sections>=1.5.2,<1.6",
        "armstrong.core.arm_wells>=1.7.0,<1.8",
        "armstrong.apps.articles>=1.1.1,<1.2",
        "armstrong.apps.content>=1.0.2,<1.1",
        "armstrong.apps.donations>=1.0.0,<1.1",
        "armstrong.apps.images>=1.1.1,<1.2",
        "armstrong.apps.related_content>=2.0.1,<2.1",
        "armstrong.hatband>=1.3.0,<1.4",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
