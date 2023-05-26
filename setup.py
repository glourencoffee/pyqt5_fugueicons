from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='pyqt5_fugueicons',
    version='3.5.6.2',
    description='Fugue Icons for PyQt5',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Giovanni Lourenço',
    author_email='gvnl.developer@outlook.com',
    url='https://github.com/glourencoffee/pyqt5_fugueicons',
    license='MIT',
    packages=['pyqt5_fugueicons'],
    keywords=['pyqt5', 'icons'],

    install_requires=['PyQt5'],

    python_requires='>=3.6'
)