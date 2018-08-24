import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fr:
    requirements = fr.read().splitlines()

setuptools.setup(
    name="beets-pitchfork",
    version="0.0.6",
    author="Filipe Fortes",
    author_email="accounts@fortes.com",
    description="Pitchfork rating plugin for beets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fortes/beets-pitchfork",
    license='MIT',
    platforms='ALL',
    packages=['beetsplug'],
    include_package_data=True,
    namespace_packages=['beetsplug'],
    install_requires=requirements,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Players :: MP3",
        "Environment :: Console",
    ])
