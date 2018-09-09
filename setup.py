from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='gym_hanoi',
      version='0.0.1',
      author='Robert Tjrako Lange',
      author_email='robert.t.lange@web.de',
      license='MIT',
      description="An OpenAI Gym Environment for the Towers of Hanoi Problem.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/RobertTLange/gym-hanoi",
      install_requires=['gym']
      )
