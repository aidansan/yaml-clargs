import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yaml-clargs",
    version="0.0.1",
    author="Aidan San",
    author_email="aidan.w.san@gmail.com",
    description="Reads in parameters from a yaml file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aidansan/yaml-clargs",
    project_urls={
        "Bug Tracker": "https://github.com/aidansan/yaml-clargs/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.5",
)