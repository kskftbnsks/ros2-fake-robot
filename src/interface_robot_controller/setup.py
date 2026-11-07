from setuptools import find_packages, setup

package_name = 'interface_robot_controller'

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
    maintainer='kskftbnsks',
    maintainer_email='furkanyaran500@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'fake_robot = interface_robot_controller.fake_robot:main',
            'monitor = interface_robot_controller.monitor:main',
        ],
    },
)
