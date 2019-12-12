from distutils.core import setup

setup(
    name = 'landdox',
    packages = ['landdox'],
    version = '1.0',  # 
    description = 'Simple wrapper around LandDox API',
    author = 'Nathan Duncan',
    author_email = 'nduncan@fifthpartners.com',
    url = 'https://github.com/natefduncan/landdox',
    download_url = 'https://github.com/natefduncan/landdox/archive/1.0.tar.gz',
    keywords = ['landdox', 'oil'],
    install_requires=['requests', 'pandas'],
    classifiers = [
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" 
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)

