import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='adh_sample_library_preview',
    version='0.9.3_preview',
    author='OSIsoft',
    license='Apache 2.0',
    author_email='samples@osisoft.com',
    description='A preview of an ADH (Aveva Data Hub) client library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/osisoft/sample-adh-sample_libraries-python',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests>=2.28.0',
        'python-dateutil>=2.8.2',
        'jsonpatch>=1.32'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    obsoletes=['ocs_sample_library_preview']
)
