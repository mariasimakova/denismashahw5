from setuptools import setup, find_packages

setup(
    name="denis_masha_library_hw5",
    version="0.1",
    description="hw5",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Maria Simakova",
    author_email="maria.simakova@bse.eu",
    url="https://github.com/mariasimakova/denismashahw5",  
    packages=find_packages(),
    install_requires=[
        "pathlib",
        "pandas",
        "scikit-learn",
    ],
    python_requires='>=3.12',
)