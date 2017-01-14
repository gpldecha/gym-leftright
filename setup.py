from setuptools import setup
from setuptools import find_packages

setup(name='gym_leftright',
      version='0.0.1',
      author='Guillaume de Chambrier',
      author_email='chambrierg@gmail.com',
      description='Left or right control environment for openai/gym',
      packages=find_packages(),
      url='https://github.com/gpldecha/gym-leftright',
      license='MIT',
      install_requires=['gym']
)


#package_dir={'gym_leftright' : 'gym_leftright/envs'},
