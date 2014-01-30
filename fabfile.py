import os
from fabric.api import *
from fabric.contrib.console import confirm

env.colorize_errors = True
env.root = '/webapps/idv'
env.virtualenv = 'idv'
env.virtualenv_args = '--clear'
env.environtment = 'develop'
env.project = 'indeverkoop'
env.repo = 'git@github.com:huiser/indeverkoop.git'

def bootstrap():
    """ initialize remote host environment (virtualenv, deploy, update) """
    require('root', provided_by=('test', 'acceptance', 'production'))
    code_dest = os.path.join(env.root, env.project)
    requirements_file = os.path.join(code_dest, 'requirements', '%s.txt' % env.environment)
    run('rm -rf %s' % code_dest)
    run('git clone %s %s' % (env.repo, code_dest))
    run('mkdir -p %(root)s' % env)
    run('mkdir -p %s' % os.path.join(env.root, 'log'))
    with prefix('. /etc/bash_completion.d/virtualenvwrapper'):
        run('mkvirtualenv %(virtualenv_args)s %(virtualenv)s' % env)
        with prefix('workon %(virtualenv)s' % env):
            with cd(code_dest):
                run('git checkout %s' % env.branch)
                run('pip install --requirement %s ' % requirements_file)
                run('./idv/manage.py syncdb')


    #create_virtualenv()
    #clone()
    #update_requirements()
    #syncdb()

def create_virtualenv():
    """ setup virtualenv on remote host """
    with prefix('. /etc/bash_completion.d/virtualenvwrapper'):
        run('mkvirtualenv %(virtualenv_args)s %(virtualenv)s' % env)

def clone():
    require('branch', provided_by=('test', 'acceptance', 'production'))
    require('repo', provided_by=('test', 'acceptance', 'production'))
    code_dest = os.path.join(env.root, env.project)
    run('rm -rf %s' % code_dest)
    run('git clone --branch %s %s %s' % (env.branch, env.repo, code_dest))
    with prefix('. /etc/bash_completion.d/virtualenvwrapper'):
        with prefix('workon %(virtualenv)s' % env):
            with cd(code_dest):
                run('./idv/manage.py syncdb')

def pull():
    code_dest = os.path.join(env.root, env.project)
    with cd(code_dest):
        run('git pull')

def migrate():
    code_dest = os.path.join(env.root, env.project)
    with cd(code_dest):
        run('./idv/manage.py migrate')

def syncdb():
    code_dest = os.path.join(env.root, env.project)
    with cd(code_dest):
        run('./idv/manage.py syncdb')

def restart_uwsgi():
    sudo('restart idv')

def deploy(version):
    require('root', provided_by=('test', 'acceptance', 'production'))
    code_dest = os.path.join(env.root, env.project)
    if env.environment == 'production':
        if not confirm('Are you sure you want to deploy production?', default=False):
            utils.abort('Production deployment aborted.')
    with cd(code_dest):
        run('git pull')
        run('git checkout v%s' % version)
    #with prefix('. /etc/bash_completion.d/virtualenvwrapper'):
    #    with prefix('workon %(virtualenv)s' % env):


def update_requirements():
    """ update external dependencies on remote host """
    #require('code_root', provided_by=('staging', 'production'))
    code_dest = os.path.join(env.root, env.project)
    #requirements_file = '%s.txt' % env.branch
    requirements_file = os.path.join(code_dest, 'requirements', '%s.txt' % env.environment)
    virtualenv_dest = os.path.join(env.root, env.virtualenv)
    with prefix('. /etc/bash_completion.d/virtualenvwrapper'):
        with prefix('workon %(virtualenv)s' % env):
            run('pip install --requirement %s ' % requirements_file)

def production():
    env.environment = 'production'
    env.hosts = ['willie.huiser.nl',]
    env.branch = 'production'

def acceptance():
    env.hosts = ['fry.huiser.nl',]
    env.branch = 'master'

def test():
    env.hosts = ['slingerak.huiser.nl',]
    env.branch = 'develop'
