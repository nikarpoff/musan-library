from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='musan',
    version='0.0.1',
    author='nikarpoff',
    author_email='nik.karpov103@mail.ru',
    description='This is the module for work with mel-specs based music analitycs models.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/nikarpoff/musan-library',
    packages=find_packages(),
    install_requires=[
        'torch==2.7.0',
        'torchvision==0.22.0',
        'torchaudio==2.7.0',
        'huggingface_hub>=0.35.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: Apache License :: Version 2.0',
        'Operating System :: OS Independent'
    ],
    keywords='transformers music analitycs hugging_face ',
    project_urls={
        'GitHub': 'https://github.com/nikarpoff'
    },
    python_requires='>=3.6'
)