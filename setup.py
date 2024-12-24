from setuptools import setup, find_packages

setup(
    name="jsoncontroller",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    description="A library to simplify JSON file operations, supporting saving, loading, updating, and backing up data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="sorairo-rlf",
    author_email="your.email@example.com",
    url="https://github.com/sorairo-rlf/jsoncontroller",  # GitHubリポジトリなど
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # 対応するPythonバージョン
)