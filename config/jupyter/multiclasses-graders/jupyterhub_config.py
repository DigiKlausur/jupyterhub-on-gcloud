c = get_config()
c.JupyterHub.ip = u'192.168.22.127'
c.JupyterHub.port = 7777
c.JupyterHub.cookie_secret_file = u'/srv/jupyterhub/jupyterhub_cookie_secret'
c.JupyterHub.db_url = u'/srv/jupyterhub/jupyterhub.sqlite'
c.ConfigurableHTTPProxy.auth_token = u'/srv/jupyterhub/proxy_auth_token'
c.JupyterHub.spawner_class = 'systemdspawner.SystemdSpawner'
c.SystemdSpawner.user_workingdir = '/home/{USERNAME}'

# Limit memory and cpu usage for each user
c.SystemdSpawner.mem_limit = '1G'
c.SystemdSpawner.cpu_limit = 1.0

# create private /tmp to isolate each user info
c.SystemdSpawner.isolate_tmp = True

# Disable or enable user sudo
c.SystemdSpawner.disable_user_sudo = False
# Readonly
c.SystemdSpawner.readonly_paths = None
# Readwrite path
#c.SystemdSpawner.readwrite_paths = None

# use jupyterlab
c.Spawner.cmd = ['jupyter-labhub']
c.Spawner.default_url = '/tree'

# ser default_shell
c.SystemdSpawner.default_shell = '/bin/bash'
c.Authenticator.admin_users = {'wus', 'admin'}

c.Authenticator.whitelist = {'wus', 'admin'}
c.LocalAuthenticator.group_whitelist = {'wus-group-1', 'wus-group-2', 'wus-group-3', 'wus-group-4'} 

# load the group
# wus-group-1, 2,3 and 4 are linux group where graders and other users who want to have acces to the course
# have to be in the group and must be listed below.
c.JupyterHub.load_groups = {
    'wus-group-1': [
        'instructor1'
    ],
    'wus-group-2': [
        'instructor2'
    ],
    'wus-group-3': [
        'instructor3'
    ],
    'wus-group-4': [
        'instructor4'
    ],
}

# service_names are the name of the services where the shared courses are being distributed
# in order for graders to get access to the course.
service_names = ['shared-wus-1', 'shared-wus-2', 'shared-wus-3', 'shared-wus-4']
service_ports = [9994, 9995, 9996, 9997]
group_names = ['wus-group-1','wus-group-2','wus-group-3','wus-group-4']

# start the notebook server as a service
# wus-course-1 , 2,3 and 4 are the accounts on the pc which hold the shared course for multi graders
c.JupyterHub.services = [
    {
        'name': service_names[0],
        'url': 'http://127.0.0.1:{}'.format(service_ports[0]),
        'command': [
            'jupyterhub-singleuser',
            '--group={}'.format(group_names[0]),
            '--debug',
        ],
        'user': 'wus-course-1',
        'cwd': '/home/wus-course-1'
    }
    ,
    {
        'name': service_names[1],
        'url': 'http://127.0.0.1:{}'.format(service_ports[1]),
        'command': [
            'jupyterhub-singleuser',
            '--group={}'.format(group_names[1]),
            '--debug',
        ],
        'user': 'wus-course-2',
        'cwd': '/home/wus-course-2'
    }
    ,
    {
        'name': service_names[2],
        'url': 'http://127.0.0.1:{}'.format(service_ports[2]),
        'command': [
            'jupyterhub-singleuser',
            '--group={}'.format(group_names[2]),
            '--debug',
        ],
        'user': 'wus-course-3',
        'cwd': '/home/wus-course-3'
    }
    ,
    {
        'name': service_names[3],
        'url': 'http://127.0.0.1:{}'.format(service_ports[3]),
        'command': [
            'jupyterhub-singleuser',
            '--group={}'.format(group_names[3]),
            '--debug',
        ],
        'user': 'wus-course-4',
        'cwd': '/home/wus-course-4'
    }
]

