from setuptools import setup, find_packages

setup(
    name="prism.py",
    version="0.1.0",
    description="A Python bot framework using mineflayer on the backend",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="SnarkyDeveloper",
    author_email="snarkydeveloper@outlook.com",
    url="https://github.com/snarkydeveloper/prism.py",
    packages=find_packages(),
    install_requires=['javascript'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)