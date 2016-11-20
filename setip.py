from setuptools import setup

setup(
    name='jdong',
    version='0.0.1',
    description='JingDong UNOFFICIAL API library based on Python3',
    long_description = 'Please go to https://github.com/WiseDoge/jdong',
    author='wisedoge',
    author_email='wisedoge@outlook.com',
    url='https://github.com/WiseDoge/jdong',
    packages=[
        'jdong'
    ],
    
    include_package_data=True,
    platforms='any',
    install_requires=[
        'requests',
        'bs4',
        'lxml',
    ],
    license='apache 2.0',
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)