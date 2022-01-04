import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="cloudRunStayAwake",
    version="1.0.5",
    description="Reduce Cloud Run cold start with targetted self call",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Resousse/cloudrun-stay-awake",
    author="Resousse",
    author_email="resousegit@gmail.com",
    license="Apache 2.0",
    classifiers=[
    ],
    package_dir = {'cloudRunStayAwake' : './'},
    packages=["cloudRunStayAwake"],
    package_data = {
        'cloudRunStayAwake': ['./LICENSE', './README.md', 'cloudRunStayAwake.py']
    },
    exclude_package_data={'cloudRunStayAwake' : ["test.py"]},
    include_package_data=True,
    install_requires=["requests"],
)