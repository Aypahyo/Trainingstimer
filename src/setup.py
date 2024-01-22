from setuptools import setup

setup(
   name='trainingstimer',
   version='1.0.0',
   description='trainingstimer shows how to use setup.py',
   author='Aypahyo',
   author_email='Aypahyo@github.com',
   url='https://github.com/Aypahyo/python-trainingstimer',
   packages=['trainingstimer_core'],
   py_modules=['trainingstimer'],
   entry_points={
    'console_scripts' : [
      'trainingstimer = trainingstimer:main'
    ],
   }
)
