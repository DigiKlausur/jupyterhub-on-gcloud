c = get_config()
c.JupyterHub.ip = u'127.0.0.1'
c.JupyterHub.port = 8000
c.JupyterHub.cookie_secret_file = u'/srv/jupyterhub/jupyterhub_cookie_secret'
c.JupyterHub.db_url = u'/srv/jupyterhub/jupyterhub.sqlite'
#c.JupyterHub.proxy_auth_token = u'/srv/jupyterhub/proxy_auth_token'
c.ConfigurableHTTPProxy.auth_token = u'/srv/jupyterhub/proxy_auth_token'
c.JupyterHub.spawner_class = 'systemdspawner.SystemdSpawner'
c.SystemdSpawner.user_workingdir = '/home/{USERNAME}'
#c.JupyterHub.config_file = '/home/admin/jupyterhub_config.py'

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

c.Autheticator.admin_users = {'admin', 'mrc-grader'}
c.Autheticator.whitelist = {'admin', 'mhm_wasil', 'instructor1', 
                            'instructor2', 'student1', 'student2',
                            'mrc-grader', 'wtus-grader'}
c.LocalAuthenticator.group_whitelist = {'mrc-group'} 
#c.LocalAuthenticator.group_whitelist = {'mrc-group', 'wtus-group'} 

# sionbg and willingc have access to a shared server:
c.JupyterHub.load_groups = {
    'mrc-group': [
        'instructor1',
        'instructor2'
    ]
    #,
    #'wtus-student-group': [
    #    'instructor2'
    #]
}
service_names = ['shared-mrc-notebook', 'shared-wtus-notebook']
service_ports = [9998, 9999]
group_names = ['mrc-group']
#group_names = ['mrc-student-group', 'wtus-student-group']

# start the notebook server as a service
c.JupyterHub.services = [
    {
        'name': service_names[0],
        'url': 'http://127.0.0.1:{}'.format(service_ports[0]),
        'command': [
            'jupyterhub-singleuser',
            '--group={}'.format(group_names[0]),
            '--debug',
        ],
        'user': 'mrc-grader',
        'cwd': '/home/mrc-grader'
    }
    #,
    #{
    #    'name': service_names[1],
    #    'url': 'http://127.0.0.1:{}'.format(service_ports[1]),
    #    'command': [
    #        'jupyterhub-singleuser',
    #        '--group={}'.format(group_names[1]),
    #        '--debug',
    #    ],
    #    'user': 'wtus-grader',
    #    'cwd': '/home/wtus-grader'
    #}
]
