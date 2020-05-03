from setuptools import setup, find_packages

install_requires = [
    'opencv-python >= 4.1.0',
    'Pillow >= 6.0.0',
    'numpy >=1.16.4'
]

setup(
    name='imbo',
    version='0.1.0',

    python_requires='>=2.7',

    packages=find_packages(),
    include_package_data=True,

    author='Nitin Rai',
    author_email='mneonizer@gmail.com',
    description='A tool to plot pretty bounding boxes around objects.',
    long_description='See https://github.com/imneonizer/bounding-box for complete user guide.',
    url='https://github.com/imneonizer/bounding-box',
    install_requires=install_requires,
    license='BSD',
)
