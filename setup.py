from setuptools import setup, find_packages

requires = [
    'tkinter',
    'sqlite3',
]

setup(
    name='Bookstore',
    version='1',
    packages=find_packages(),
    keywords='python tkinter sqlite',
    url='',
    license='',
    author='Tom Hildebrand',
    author_email='t1manster@gmail.com',
    description='Bookstore application with GUI (TKinter) and database (SQLite) interaction.',
    install_requires=requires
)
