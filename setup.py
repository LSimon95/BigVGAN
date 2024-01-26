from setuptools import setup, find_packages
from pathlib import Path

project_root = Path(__file__).parent

setup(
    name='BigVGAN',
    version='0.1',
    description='BigVGAN',
    author='BigVGAN',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License"
        'Programming Language :: Python :: 3.10',
    ],
    packages=['bigvgan'],
    package_dir={'bigvgan': 'bigvgan'},
    package_data={'bigvgan': ['configs/*.json']},
    install_requires=[
        "torch",
        "numpy",
        "librosa",
        "scipy",
        "tensorboard",
        "soundfile",
        "matplotlib",
        "pesq",
        "auraloss",
        "tqdm"
    ]
)