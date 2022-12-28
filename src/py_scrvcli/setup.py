from setuptools import setup

package_name = 'py_scrvcli'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='blackcoffee',
    maintainer_email='blackcoffee@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'custom_service = py_scrvcli.custom_service_member_function:main',
            'custom_client = py_scrvcli.custom_client_member_function:main'
            'service = py_scrvcli.service_member_function:main',
            'client = py_scrvcli.client_member_function:main'

        ],
    },
)
