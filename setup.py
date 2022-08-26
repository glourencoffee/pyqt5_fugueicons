from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='pyqt5_fugueicons',
    version='3.5.6.1',
    description='Fugue Icons for PyQt5',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Giovanni L',
    author_email='callmegiorgio@hotmail.com',
    url='https://github.com/callmegiorgio/pyqt5_fugueicons',
    license='MIT',
    packages=['pyqt5_fugueicons'],
    keywords=['pyqt5', 'icons'],

    install_requires=['PyQt5'],

    python_requires='>=3.6'
)