from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

##edit below variables as per your requirements -
REPO_NAME = "Smart-Books-Recommendation-System"
AUTHOR_USER_NAME = "ishan8604"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A Small package of Smart Books Recommendation System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="ishan860484@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.11.5",
    install_requires=LIST_OF_REQUIREMENTS
)