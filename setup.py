from distutils.core import setup

setup(
    name='peewee-db-evolve',
    version=__import__('peeweedbevolve').__version__,
    description='Schema Evolution for Peewee',
    long_description='',
    author='Derek Anderson',
    author_email='public@kered.org',
    url='https://github.com/keredson/peewee-db-evolve',
    packages=[],
    py_modules=['peeweedbevolve'],
    classifiers=[
#        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: LGPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)

