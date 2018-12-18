from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='implicits',
    version='1.0.2',
    description='Implicit parameters in Python',
    long_description=long_description,
    url='https://github.com/JadenGeller/Implicits',
    author='Jaden Geller',
    license='MIT',
    packages=['implicits'],
    classifiers=['Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Topic :: Software Development :: Libraries',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python'
                 ],
    keywords='implicit implicits arguments parameters scala context locals',
    zip_safe=True)
