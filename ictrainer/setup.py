from setuptools import setup

setup(name="ictrainer",
      version="0.1.6",
      description="cli tool for training your own image classifier with one line command!",
      url="https://github.com/koji/ictrainer",
      author='koji kanao',
      author_email='koji.kanao@nyu.edu',
      license="MIT",
      packages=["ictrainer"],
      scripts=["bin/ictrainer"],
      install_requires=["docopt==0.6.2", "keras", "numpy", "tensorflow", "icrawler", "Pillow"])
