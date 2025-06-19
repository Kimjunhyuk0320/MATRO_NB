from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'MATRO_NB'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),  # ✅ launch 폴더 포함
        ('share/' + package_name + '/config', glob('config/*')),  # ✅ config 폴더도 있을 경우 포함 (선택사항)
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='junhyuk',
    maintainer_email='kimminuk0320@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_node = MATRO_NB.hello_node:main',
        ],
    },
)
