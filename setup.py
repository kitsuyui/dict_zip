from setuptools import setup


setup(
    name='dict_zip',
    version='0.1.0',
    description='zip and zip_longest for dict',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yui Kitsu',
    author_email='kitsuyui+github@kitsuyui.com',
    url='https://github.com/kitsuyui/dict_zip',
    packages=[
        'dict_zip',
    ],
    package_dir={
        'dict_zip': 'dict_zip',
    },
    package_data={
        '': ['README.md', 'LICENSE'],
        'dict_zip': ['py.typed'],
    },
    install_requires=[],
    extras_require={},
    tests_require=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
    test_suite='tests',
    license='BSD-3-Clause',
)
