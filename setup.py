from setuptools import setup, find_packages

setup(
        name='CovidVoting',
        version='__version__ 1.0',
        description='This is the setup for CovidVoting Module',
        author='Chiaoya Chang, Yanyan Guan. Lindsey Ulmer',
        author_email='chiaoya@uw.edu',
        LICENSE = "MIT",
        url='https://github.com/lindseyulmer/Voting-COVID', 
        packages=find_packages(),
        package_dir={'CovidVoting': 'CovidVoting'},
        package_data={'CovidVoting': ['data/*']},
        requires = ["pandas", "NumPy", "geopandas", "bokeh"]
)