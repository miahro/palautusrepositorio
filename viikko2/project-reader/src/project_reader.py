from urllib import request
from project import Project
from toml import loads


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        project_dict = loads(content)
        name = project_dict["tool"]["poetry"]["name"]
        description = project_dict["tool"]["poetry"]["description"]
        dependencies = list(
            project_dict["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(
            project_dict["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())
        license = project_dict["tool"]["poetry"]["license"]
        authors = project_dict["tool"]["poetry"]["authors"]
        return Project(name, description, license, authors, dependencies, dev_dependencies)
