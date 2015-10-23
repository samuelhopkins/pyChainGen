from setuptools import setup

setup(name='pychainmarkov',
      version='0.1',
      description='Markov chain text psuedo random generator',
      url='http://github.com/samuelhopkins/pyChainGen',
      author='Sam Hopkins',
      author_email='sahopkins93@gmail.com',
      license='MIT',
      packages=['pychainmarkov'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)
