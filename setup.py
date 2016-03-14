from setuptools import setup


setup(
    name="GSOC McGill Institute Application",
    version="1.0.0",
    url="http://github.com/jackromo/GSOCMcgillApplication",
    license="MIT",
    author="Jack Romo",
    author_email="sharrackor@gmail.com",
    description="Software written for an application for a Google Summer of Code programme",
    platforms="any",
    packages=["mcgill_app"],
    entry_points={
        "console_scripts": ["mcgill_app = mcgill_app.main:main"],
    },
    install_requires=[
        "matplotlib>=1.5.1",
        "sphinx>=1.3.6"
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python 2.7"
    ]
)
