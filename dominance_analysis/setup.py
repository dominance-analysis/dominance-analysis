import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dominance_analysis",
    version="1.0.1",
    author="Sajan Kumar Bhagat, Kunjithapatham Sivakumar, Shashank Shekhar",
    author_email='bhagat.sajan0073@gmail.com, s.vibish@gmail.com, quintshekhar@gmail.com',
    maintainer="Sajan Kumar Bhagat, Kunjithapatham Sivakumar, Shashank Shekhar",
    maintainer_email='bhagat.sajan0073@gmail.com, s.vibish@gmail.com, quintshekhar@gmail.com',
    description='Dominance Analysis',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bhagatsajan0073/dominance_analysis',
    packages=setuptools.find_packages(),
    license='MIT',
    zip_safe=False,
    classifiers=[
        # "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'pandas',
          'numpy',
          'seaborn',
          'matplotlib',
          'scikit-learn',
          'tqdm',
          'plotly',
          'cufflinks',
          'statsmodels',
          'ipywidgets'
    ],
    include_package_data=True
)