from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.0.1",
    description="This contains code in the ./src directory for the Databricks project",
    package=find_packages(where="./src"),
    package_dir={"": "./src"},
    install_requires=['setuptools']
    entry_points = {
        "package":{
            "main": "dba_project.main:main"
        }
    }
)