from setuptools import setup

setup(
    name='sngan_projection',
    version='0.1',
    description='GANs with spectral normalization and projection discriminator',
    url='https://github.com/tanikawa04/sngan_projection',
    packages=[
        'source',
        'source.functions',
        'source.links',
        'source.miscs'
    ],
    install_requires=[
        'chainer>=3.3.0',
        'numpy>=1.11.1'
    ]
)
