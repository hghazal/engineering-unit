from datetime import datetime
from fabric.api import env, cd, run, task, prefix, sudo
from fabric.contrib.files import exists

import local_fab_settings

env.user = local_fab_settings.USER
# env.key_filename = local_fab_settings.KEY_FILENAME
env.hosts = local_fab_settings.HOSTS
env.code_dir = local_fab_settings.CODE_DIR
env.forward_agent = True
env.virtualenv = local_fab_settings.VIRTUAL_ENV_DIR
env.github_repo = local_fab_settings.GITHUB_REPO
env.webserver_supervisor_label = 'gunicorn-engineeringunit.com'


def archive_installation_if_exists():
    with cd(env.code_dir):
        if exists('repo'):
            dir_postfix = datetime.now().isoformat()
            new_dir_name = 'repo-{0}'.format(dir_postfix)
            print "Moving old install to {0}".format(new_dir_name)
            run("mv -f repo {0}".format(new_dir_name))


def check_if_installation_exists():
    with cd(env.code_dir):
        if exists('repo'):
            raise Exception("Application is already installed.")


def setup_installation():
    with cd(env.code_dir):
        # checkout the code
        run('git clone git+ssh://git@github.com/{0}.git repo'.format(env.github_repo))
        run('cd .. && ln -sf repo current')


def install_requirements():
    with prefix('source {0}bin/activate'.format(env.virtualenv)):
        with cd(env.code_dir):
            with cd('repo'):
                # install the requirements in the virtualenv
                run('pip install -r requirements.txt')


def update_code_from_github(tag="master"):
    with prefix('source {0}bin/activate'.format(env.virtualenv)):
        with cd(env.code_dir):
            with cd('repo'):
                run('git fetch')
                run('git checkout {0}'.format(tag))
                run('git pull --rebase origin {0}'.format(tag))


@task
def restart_webserver():
    sudo('supervisorctl restart {0}'.format(env.webserver_supervisor_label), shell=False)


@task
def update_database():
    """ Update and migrate database schema. """
    with prefix('source {0}bin/activate'.format(env.virtualenv)):
        with cd(env.code_dir):
            with cd('repo'):
                run('python ./manage.py syncdb --noinput --migrate')


@task
def collectstatic():
    """ Collect static files. """
    with prefix('source {0}bin/activate'.format(env.virtualenv)):
        with cd(env.code_dir):
            with cd('repo'):
                run('python ./manage.py collectstatic --noinput')

@task
def compress():
    """ Run django compress. """
    with prefix('source {0}bin/activate'.format(env.virtualenv)):
        with cd(env.code_dir):
            with cd('repo'):
                run('DOMAIN="prod" python ./manage.py compress --force')

@task
def compile_pyc():
    """ Run django compile_pyc """
    with prefix('source {0}bin/activate'.format(env.virtualenv)):
        with cd(env.code_dir):
            with cd('repo'):
                run('python ./manage.py compile_pyc')

@task
def ls():
    """ Run django compress. """
    run('ls -la')

@task
def provision():
    """ Installs the eu app. """
    check_if_installation_exists()
    setup_installation()


@task
def deploy(tag="master"):
    """ Deploys a specified `tag`. """
    print "Deploying tag: {0}".format(tag)
    print "Running as user: {0}".format(env.user)

    update_code_from_github(tag)
    install_requirements()
    # update_database()
    collectstatic()
    compress()
    compile_pyc()
    restart_webserver()


@task
def archive():
    """ Archives the current installation to a timestamped folder. """
    archive_installation_if_exists()
