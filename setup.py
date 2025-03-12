from setuptools import setup, find_packages, setup

setup(
    name = 'macqgenerator',
    version = '0.0.1',
    author = "Abhi",
    author_email="abhishekmirji24@gmail.com",
    install_requires = ["openai", "langchain","streamlit", "python-dotenv", "PyPDF2"],
    packages = find_packages()
)
