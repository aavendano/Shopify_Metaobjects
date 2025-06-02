from setuptools import setup, find_packages

setup(
    name="shopify-metaobject-loader",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "requests>=2.26.0",
        "python-dotenv>=0.19.0",
        "tenacity>=8.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python module for loading data into Shopify metaobjects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/shopify-metaobject-loader",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
) 