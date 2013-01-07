from setuptools import setup, find_packages

setup(name="ScreenCaptureLibrary",
      version="0.1dev",
      packages=['ScreenCaptureLibrary'],
      #packages=find_packages("src"),
      package_dir={'ScreenCaptureLibrary': 'src/ScreenCaptureLibrary'},
      include_package_data=True,
      zip_safe=False,
      keywords='',
      author='',
      author_email='',
      url='https://github.com/emanlove/robotframework-screencapturelibrary',
      license='',
     )
