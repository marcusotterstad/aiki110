from setuptools import find_packages, setup

package_name = 'maott4996_agenter'

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
    maintainer='maott4996',
    maintainer_email='maott4996@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lysdiodenode = maott4996_agenter.lysdiodenode:main',
            'bevegelsesnode = maott4996_agenter.bevegelsesnode:main',
            'motornode = maott4996_agenter.motornode:main',
        ],
    },
)
