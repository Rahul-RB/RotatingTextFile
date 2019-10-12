import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RotatingTextFile",
    version="0.0.2",
    description="A ZERO dependency rotating file handler which rotates when YOU want it to, rather than based on bytes size.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Console',
        'Natural Language :: English',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Intended Audience :: Developers",
    ],
    keywords='custom rotating file handler textfile logger',
    author='Rahul R Bharadwaj',
    author_email='rahulbharadwaj033@gmail.com',
    url='https://github.com/Rahul-RB/RotatingTextFile',
    packages=setuptools.find_packages(exclude=['examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)