import sys
from setuptools import setup, find_packages

with open('readme.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

info = sys.version_info

setup(name="ictrainer",
      version="0.2.7",
      description="cli tool for training your own image classifier with one line command!",
      long_description=readme,
      long_description_content_type='text/markdown',
      url="https://github.com/koji/ictrainer",
      author='koji kanao',
      author_email='koji.kanao@nyu.edu',
      license="MIT",
      packages=["ictrainer"],
      scripts=["bin/ictrainer"],
      install_requires=["docopt==0.6.2", "keras", "numpy", "tensorflow", "icrawler", "Pillow", "opencv-python", "numpy", "matplotlib"])
