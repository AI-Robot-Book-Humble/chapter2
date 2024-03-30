from setuptools import find_packages, setup

package_name = 'happy_parameter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='demura@neptune.kanazawa-it.ac.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'happy_parameter_server_node = happy_parameter.happy_parameter_server_node:main',
            'happy_parameter_client_node = happy_parameter.happy_parameter_client_node:main',
        ],
    },
)
