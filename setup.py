from setuptools import setup, find_packages

# Leer el contenido de README.md para la descripción larga
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Leer las dependencias desde requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="shopify-metaobject-loader",
    version="0.1.0",
    author="Alejandro", # Puedes cambiar esto
    author_email="tu_email@example.com", # Y esto
    description="Un cargador de metaobjetos de Shopify para interactuar con la API Admin GraphQL.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu_usuario/Shopify_Metaobjects", # URL a tu repositorio
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)