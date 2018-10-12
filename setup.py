from setuptools import setup, find_packages

required_packages = ["graphql-core>=2.1", "quart>=0.6.7", "graphql-server-core>=1.1"]

setup(
    name="Quart-GraphQL",
    version="2.0.0",
    description="Adds GraphQL support to your Quart application",
    long_description=open("README.rst").read(),
    url="https://github.com/MarkJGx/quart-graphql",
    download_url="https://github.com/MarkJGx/quart-graphql/releases",
    author="Syrus Akbary, MarkJGx",
    author_email="contact@markjg.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="api graphql protocol rest quart",
    packages=find_packages(exclude=["tests"]),
    install_requires=required_packages,
    tests_require=["pytest>=2.7.3"],
    include_package_data=True,
    zip_safe=False,
    platforms="any",
)
