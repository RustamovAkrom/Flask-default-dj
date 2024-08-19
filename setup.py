from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Flask-Default_DJ",
    version="0.1",
    author="Akrom Rustamov",
    author_email="akromjonrustamov56@gmail.com",
    description="Flask Default Django.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "Flask==3.0.2",
        "Flask-Admin==1.6.1",
        "flask-babel==4.0.0",
        "Flask-Bcrypt==1.0.1",
        "Flask-Bootstrap==3.3.7.1",
        "Flask-Limiter==3.8.0",
        "Flask-Login==0.6.3",
        "Flask-Mail==0.10.0",
        "Flask-Migrate==4.0.7",
        "Flask-SQLAlchemy==3.1.1",
        "Flask-Testing==0.8.1",
        "Flask-Uploads==0.2.1",
        "Flask-WTF==1.2.1",
    ],
    classifiers=[
        "Programing Language :: Python :: 3",
        "License :: OSI Approved :: MIT license",
    ]
)
