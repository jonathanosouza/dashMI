from setuptools import setup, find_packages

setup(
    name="vendas-cli",
    version="0.1.0",
    description="Gerador de relatório Mirante Tecnologia",
    author="Jonathan de Oliveira Souza Filho",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "vendas-cli = vendas_cli.__main__:main"
        ]
    },
    python_requires=">=3.10",
)
