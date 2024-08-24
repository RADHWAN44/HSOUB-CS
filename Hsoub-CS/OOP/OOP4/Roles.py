class ProgrammerRole:
    def __init__(self, lang, projects):
        self.lang = lang
        self.projects = projects

    def assign_project(self, project):
        self.projects.append(project)

    def get_projects(self):
        print('Projects: ')
        print('=' * 10)
        projects_lest = []
        for project , nomber in enumerate(self.projects):
            projects_lest.append(f'{nomber + 1} {project}')
        return '\n'.join(projects_lest)


class DesignerRole:
    def __init__(self, apps, progects):
        self.apps = apps
        self.projects = progects


    def assign_project(self, project):
        self.projects.append(project)

    def get_projects(self):
        print('Projects: ')
        print('=' * 10)
        projects_lest = []
        for project , nomber in enumerate(self.projects):
            projects_lest.append(f'{nomber + 1} {project}')
        return '\n'.join(projects_lest)