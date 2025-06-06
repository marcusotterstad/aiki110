from setuptools import find_packages, setup

package_name = 'maott4996_bryter'

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
            'bryter_service = maott4996_bryter.bryter_service:main',
            'bryter_monitor = maott4996_bryter.bryter_monitor:main'
        ],
    },
)
