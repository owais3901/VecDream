from distutils.core import setup

setup(
    name='VecDream',
    packages=['VecDream'],
    version='0.1',
    license='MIT',
    description='Basic Library',
    author='Owais',
    author_email='b19102090@gmail.com',
    url='https://github.com/owais3901/VecDream.git',
    keywords=['Vector Database'],
    install_requires=[
        'sentence-transformers',
    ],
    python_requires='>=3.6',  # Requires any version >= 3.6

    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
    ],
)