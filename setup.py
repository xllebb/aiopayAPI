from setuptools import setup, find_packages


with open('README.md', encoding="utf-8") as f:
  long_description = f.read()


setup(
  name='aiopayAPI',
  version='0.1.4',
  author='xllebb',
  author_email='090504opo@gmail.com',
  description='Асинхронный API для работы с платежной системой Payok.io.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/xllebbSQ/aiopayAPI',
  packages=find_packages(),
  install_requires=['aiohttp>=3.8.5',
                    "asyncio>=3.4.3",
                    "typing>=3.7.4",],
  classifiers=[
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='python PayOk payok api API asyncio payok api',
  python_requires='>=3.8'
)