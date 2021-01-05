from setuptools import setup
from setuptools import find_packages

setup(
    name="emojipastabot",
    version="1.0.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages("emojifier"),
    package_dir={"": "emojifier"},
    package_data={"": ["*.txt", "*.json"]},
    include_package_data=True,
    install_requires=["emoji", "praw>=5.0.0,<6.0.0"],
)
