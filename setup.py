from setuptools import setup, find_packages

setup(
    name="HiCity",
    author="Waitti",
    version="1.0",
    install_requires=["attrs>=19.3.0", "autopep8>=1.5.2", "backcall>=0.1.0", "bleach>=3.1.4", "certifi>=2020.4.5.1",
                      "cffi>=1.14.0", "chardet>=3.0.4", "click>=7.1.1", "colorama>=0.4.3", "decorator>=4.4.2",
                      "defusedxml>=0.6.0", "entrypoints>=0.3", "Flask>=1.1.2", "gevent>=20.5.0", "greenlet>=0.4.15",
                      "idna>=2.9", "importlib-metadata>=1.6.0", "ipykernel>=5.2.1", "ipython>=7.13.0",
                      "ipython-genutils>=0.2.0", "ipywidgets>=7.5.1", "itsdangerous>=1.1.0", "jedi>=0.17.0",
                      "Jinja2>=2.11.2", "jsonschema>=3.2.0", "jupyter-client>=6.1.3", "jupyter-console>=6.1.0",
                      "jupyter-core>=4.6.3", "MarkupSafe>=1.1.1", "mistune>=0.8.4", "nbconvert>=5.6.1",
                      "nbformat>=5.0.6", "notebook>=6.0.3", "pandocfilters>=1.4.2", "parso>=0.7.0",
                      "pickleshare>=0.7.5", "prometheus-client>=0.7.1", "prompt-toolkit>=3.0.5", "pycodestyle>=2.5.0",
                      "pycparser>=2.20", "Pygments>=2.6.1", "PyQt5>=5.12.3", "PyQt5-sip>=4.19.18",
                      "PyQtWebEngine>=5.12.1", "pyrsistent>=0.16.0", "python-dateutil>=2.8.1", "pywin32>=227",
                      "pywinpty>=0.5.7", "pyzmq>=19.0.0", "qtconsole>=4.7.3", "QtPy>=1.9.0", "requests>=2.23.0",
                      "Send2Trash>=1.5.0", "six>=1.14.0", "SQLAlchemy>=1.3.16", "terminado>=0.8.3", "testpath>=0.4.4",
                      "tornado>=6.0.4", "traitlets>=4.3.3", "urllib3>=1.25.8", "wcwidth>=0.1.9", "webencodings>=0.5.1",
                      "Werkzeug>=1.0.1", "widgetsnbextension>=3.5.1", "wincertstore>=0.2", "XlsxWriter>=1.2.8",
                      "zipp>=3.1.0"],
    description="HiCity",
    packages=find_packages()
)
# python setup.py sdist bdist_wheel
