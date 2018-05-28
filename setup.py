from distutils.core import setup


setup(name = 'GeoJsonCSVJoin',
      version = '0.0.1',
      description = 'Merge GeoJSON to multiple CSV files',
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Environment :: Python Interpreter',
          'License :: None',
          'Operating System :: OS Independent',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Topic :: Text Processing :: Filters',
          'Topic :: Utilities'
      ],
      author = 'Harry Maher',
      author_email = 'HarryB.Maher@gmail.com',
      url = 'https://github.com/HarryMaher/GeoJsonCSVJoin',
      packages = ['GeoJsonCSVJoin'],
      requires = [
          'json'
      ],
      scripts= [
          'GeoJsonCSVJoin.py'
      ],
      )
