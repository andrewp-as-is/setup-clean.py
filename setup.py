import setuptools

setuptools.setup(
    name='setup-clean',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/setup-clean']
)
