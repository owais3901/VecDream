from setuptools import setup, find_packages

setup(
    name="VecDream",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "sentence_transformers",
        # Add other dependencies as needed
    ],
    entry_points={
        "console_scripts": [
            "VecDream=VecDream",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
