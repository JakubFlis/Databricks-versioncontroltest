from setuptools import setup

setup(name='trainmodel',
      version='0.11',
      description='Databricks model train test',
      long_description='',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='databricks trainmodel',
      author='Databricks TrainModel',
      author_email='databrickstrainmodel@example.com',
      license='MIT',
      packages=['trainmodel'],
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['trainmodel-job=trainmodel.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
