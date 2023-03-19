from setuptools import find_packages, setup

NAME = "aura.ai"
VERSION = "0.1.0"
DESCRIPTION = "A Python library to transcribe and summarize voice recordings."

# loading readme
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# setting up
setup(
    name=NAME,
    version=VERSION,
    author="Rafael Gallardo",
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "soundfile",
        "soundcard",
    ],
    extras_require={
        "dev": [
            "pre-commit",
        ],
    },
    keywords=["aura.ai"],
    classifiers=[
        "Development Status :: Alpha",
        "Operating System :: OS Independent",
        "License :: Undefined",
    ],
)