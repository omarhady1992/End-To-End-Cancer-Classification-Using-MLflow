import setuptools

with open('README.md', "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-To-End-Cancer-Classification-Using-MLflow"
AUTHOR_USER_NAME = "omarhady1992"
SRC_REPO = "End-To-End-Cancer-Classification-Using-MLflow"
AUTHOT_EMAIL = "ohady1992@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOT_EMAIL,
    description="A package to use CNN to classifiy chest cancer",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)