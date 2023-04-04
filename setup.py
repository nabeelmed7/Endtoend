from setuptools import find_packages, setup
from typing import List

_e_ = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if _e_ in requirements:
            requirements.remove(_e_)
    return requirements


setup(
name = 'MLProject',
version = '0.0.1',
author = 'Mohammed Ahmed',
author_email = 'beelkaahmed@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)