import click
from .core import Djirun

@click.command()
@click.argument('project_name')
@click.option('--css-framework', default='none', help='Framework CSS à utiliser (bootstrap, tailwind, none)')
@click.option('--static-structure/--no-static-structure', default=False, help='Créer une structure de fichiers statiques')
@click.option('--single-page/--no-single-page', default=False, help='Créer une application en page unique')
@click.option('--database', default='sqlite', help='Base de données à utiliser (sqlite, postgres)')
@click.option('--auth/--no-auth', default=False, help='Activer l\'authentification')
@click.option('--api/--no-api', default=False, help='Activer l\'API REST')
@click.option('--i18n/--no-i18n', default=False, help='Activer l\'internationalisation')
@click.option('--tests/--no-tests', default=False, help='Ajouter des tests unitaires')
@click.option('--docs/--no-docs', default=False, help='Générer la documentation')
@click.option('--docker/--no-docker', default=False, help='Ajouter la configuration Docker')
@click.option('--python-version', default=None, help='Version de Python à utiliser pour Docker')

def main(project_name, css_framework, static_structure, single_page, database, auth, api, i18n, tests, docs, docker, python_version):
    """Creation et configuration d'un projet Django avec diverses options."""
    # Creating a Djirun Instance
    djirun = Djirun(
        project_name=project_name,
        css_framework=css_framework,
        static_structure=static_structure,
        single_page=single_page,
        database=database,
        auth=auth,
        api=api,
        i18n=i18n,
        tests=tests,
        docs=docs,
        docker=docker,
        python_version=python_version
    )
    # Django Config and Creation
    djirun.handle()

if __name__ == '__main__':
    main()
