from distutils.core import setup
setup(
  name = 'Topsis-Aryaman-101903495',
  packages = ['Topsis-Aryaman-101903495'],
  version = '0.1',
  license='MIT',
  description = 'This is a package for python where user has to input the csv file and weight and impacts and get the topsis ranking as a csv file output',
  author = 'Aryaman Choudhary',
  author_email = 'aryaman.choudhary01@gmail.com',
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Topsis', 'Ranking',],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
