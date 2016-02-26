try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
cofig = {
    'description': 'My Project',
    'author': 'Peter Chen',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': '50590960@qq.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**cofig)