from setuptools import setup

setup(
    name='vectorbt',
    version=0.6,
    description='Python library for backtesting trading strategies at scale',
    author='Oleg Polakow',
    author_email='olegpolakow@gmail.com',
    url='https://github.com/polakowo/vectorbt',
    packages=['vectorbt'],
    install_requires=['numpy', 'pandas', 'matplotlib', 'ipywidgets', 'plotly', 'numba>=0.49.0']
)
