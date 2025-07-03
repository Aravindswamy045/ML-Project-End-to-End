from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns list of requirements
    '''
    requiremenets=[]
    with open(file_path) as file_obj:
        requiremenets=file_obj.readlines()
        requiremenets=[req.replace("\n","") for req in requiremenets]
        if HYPEN_E_DOT in requiremenets:
            requiremenets.remove(HYPEN_E_DOT)
    return requiremenets

setup(
    name='mlproject',
    version='0.0.1',
    author='Aravind',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))


