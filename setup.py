from setuptools import setup

setup(
    name='httpie-image',
    description='iTerm2 image display plugin for HTTPie.',
    version='1.0.0',
    author='banteg',
    url='https://github.com/banteg/httpie-image',
    py_modules=['httpie_image'],
    install_requires=['httpie'],
    entry_points={
        'httpie.plugins.converter.v1': [
            'httpie_image = httpie_image:ImagePlugin',
        ]
    },
)
