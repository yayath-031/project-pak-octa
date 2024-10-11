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
  version='0.1.2',
  description='Mencari referensi dengan cepat',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url_git='https://github.com/yayath-031/project-pak-octa.git',  
  author='Kiyowo Team',
  author_email='yaynature01@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='film', 
  packages=find_packages(),
  install_requires=[''] 
)