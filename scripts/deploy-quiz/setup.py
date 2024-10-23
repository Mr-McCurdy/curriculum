# curriculum/scripts/deploy-quiz/setup.py

from setuptools import setup, find_packages

setup(
    name='quiz_lib',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A library for creating and managing quizzes in Canvas.',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    python_requires='>=3.6',
)