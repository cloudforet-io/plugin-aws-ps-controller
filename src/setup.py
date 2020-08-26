from setuptools import setup, find_packages
 
with open('VERSION', 'r') as f:
    VERSION = f.read().strip()
    f.close()
 
setup(
    name='plugin-aws-power-scheduler-controller',
    version=VERSION,
    description='AWS plugin for power scheduler',
    long_description='',
    author='Jin',
    author_email='smiler.jin@samsung.com',
    packages=find_packages(),
    install_requires=[
        'spaceone-core',
        'spaceone-api',
        'spaceone-tester',
        'boto3',
        'schematics'
    ],
    zip_safe=False,
)
