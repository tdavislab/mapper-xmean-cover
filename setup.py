import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setuptools.setup(
    name="mapper_xmean_cover", 
    version="0.1.0",
    author="Nithin Chalapathi",
    author_email="",
    description="Package alongside 'Adaptive Covers for Mapper Graphs Using Information Criteria'.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tdavislab/mapper-xmean-cover/",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
)
