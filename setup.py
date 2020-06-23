import setuptools

setuptools.setup(
    name="nb_eliza",
    packages=['eliza'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'notebook'
    ],
    data_files=[],
    zip_safe=False
)