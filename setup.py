from distutils.core import setup
setup(
    name="indodax",  # How you named your package folder (MyLib)
    packages=["indodax"],  # Chose the same as "name"
    version="1.0.0",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    # Give a short description about your library
    description="Python wrapper for indodax.com API",
    author="Bernard Siahaan",  # Type in your name
    author_email="bernard.siahaan.xy@gmail.com",  # Type in your E-Mail
    # Provide either the link to your github or to your website    keywords = ["indodax", "vipbtc", "api"], # Keywords that define your package best
    url="https://github.com/SiahaanBernard/pyndodax",
    install_requires=[  # I get to this in a second
        "requests",
        "pandas"
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]
)
