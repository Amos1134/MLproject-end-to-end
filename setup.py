from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return list of all requirements for the application

    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
name="mlproject_endtoend",
version="0.0.1",
author="Amos",
author_email="aamosaadesuyi@yahoo.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt') 
)