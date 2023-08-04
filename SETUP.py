from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("VERSION", "r") as f:
    version = f.read().strip()


setup(
    name="progrming0804",
    version=version,
    author="Donggeun.Lee",
    author_email="dgmath8@naver.com",
    description="KNUE_TEST",
    url="https://github.com/dgmath8/programing0804",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
