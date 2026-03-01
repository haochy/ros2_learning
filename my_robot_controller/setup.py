from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hao',
    maintainer_email='haocy9264@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'test_node = my_robot_controller.test_node:main',
            'draw_circle = my_robot_controller.draw_circle:main',
            'pose_sub = my_robot_controller.pose_sub:main',
            'turtle_controller = my_robot_controller.turtle_controller:main',
            'param_controller = my_robot_controller.param_controller:main',
        ],
    },
)
