from setuptools import find_packages, setup


def get_req():
    """Reads requirements.txt and returns a list of requirements

    Returns:
        list: list of requirements
    """
    with open("requirements.txt", mode="r") as f:
        requirements = f.readlines()
    # Ignore --extra-index-url parameters in requirements.txt
    requirements = [r.strip().split(" ")[-1] for r in requirements]
    return requirements

setup(
    name="api_manager",
    version="0.1.0",
    description="Assignement",
    author="Mattia Federici",
    author_email="m.federici006@gmail.com",
    packages=find_packages("."),
    license="MIT",
    python_requires=">3",
    install_requires=get_req(),

)
