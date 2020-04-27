from setuptools import setup, find_packages

setup(
    name="HiCity",
    author="Waitti",
    version="0.9",
    install_requires=["certifi>=2020.4.5.1", "chardet>=3.0.4", "click>=7.1.1", "Flask>=1.1.2", "idna>=2.9",
                      "itsdangerous>=1.1.0", "Jinja2>=2.11.2", "MarkupSafe>=1.1.1", "requests>=2.23.0",
                      "SQLAlchemy>=1.3.16", "urllib3>=1.25.8", "Werkzeug>=1.0.1", "wincertstore>=0.2",
                      "XlsxWriter>=1.2.8"],
    description="HiCity",
    packages=find_packages()
)
# python setup.py sdist bdist_wheel
