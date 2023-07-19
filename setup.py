from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='image-file-validator',
  version='0.0.4',
  description='A simple pluggable image file validator for all type of python applications',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/Zeecoworld/image-file-validator',  
  author='Isaac Yakubu',
  long_description_content_type='text/markdown',
  author_email='engrisaac1234@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='image-validate,image,image file validation', 
  packages=find_packages(),
  install_requires=['filetype'] 
)

