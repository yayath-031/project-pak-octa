from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='himaaaa',
  version='0.2.1',
  description='Mencari referensi dengan cepat',
  long_description=open('README.md', 'r', encoding='utf-8').read(),
  long_description_content_type='text/markdown',
  url_git='https://github.com/yayath-031/project-pak-octa.git',  
  author='Kiyowo Team',
  author_email='yaynature01@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='film, reference, series, movie, comic, song, game, novel', 
  packages=find_packages(),
  install_requires=[''] 
)