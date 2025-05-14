from setuptools import find_packages, setup

package_name = 'omx_commander'

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
    maintainer='MASUTANI Yasuhiro',
    maintainer_email='at-home-book@googlegroups.com',
    description='Commander for open_manipulator',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'topic_joint = omx_commander.topic_joint:main',
            'moveit_servo = omx_commander.moveit_servo:main',
            'moveit_input = omx_commander.moveit_input:main',
            'moveit_tf = omx_commander.moveit_tf:main',
        ],
    },
)
