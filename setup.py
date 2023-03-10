import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dnastore",
    version="0.1.0",
    author="wovago",
    author_email="9787439+wovago@users.noreply.github.com",
    description="Python package for DNA storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wovago/dnastore",
    project_urls={
        "Bug Tracker": "https://github.com/wovago/dnastore/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
