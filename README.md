This project consists of configs to deploy jupyterhub for teaching on Google Cloug Engine capable of handling 50 to 60 students. It uses systemd spawner to spawn users.
However, due to unreliability of a single server running jupyterhub, we are switching to [Kubernetes](https://github.com/DigiKlausur/jupyterhub-on-kubernetes).
This deployment is useful for small class consisting of maximum 50-60 students.

Installation
============
Created Freitag 21 September 2018


* Create instance on google vm
  * VM Instance
    * Change server to europe-west1-b
    * Costumize cpu and memory
    * Choose boot disk and change the disk size
    * Firewall: allow http and https traffic
  * Snapshot
    * Create a snapshot for backup
  * IP external
    * Create reserved static ip
    * Attach static ip to the instance
  * Create a domain name

* On the instance
  * Install nginx: sudo apt install nginx
  * Install certbot
    * Go to: <https://certbot.eff.org/lets-encrypt/debianstretch-nginx>
    * Install: sudo apt-get install python-certbot-nginx -t stretch-backports
    * Obtain ssl certificate (got certbot url)
        * sudo certbot certonly --authenticator standalone --pre-hook "nginx -s stop" --post-hook "nginx"
	* Configure let's encript
	* cd [/etc/letsencrypt](file:///etc/letsencrypt)
	* sudo chmod 777 -R archive/
	* sudo chmod 777 -R live/
    * Shutdown pc, and configure cloud dns in gcloud and in your dns provider
      * In your dns provider
      * Add A record in the name server that points to your ip address
      * In google dns cloud
        * Create zone and add your domain and your name server (A, NS and CNAME record)
  * Create cookie secret, proxy auth token and dhparam.pem for jupyterhub 
    * Create cookie secret
      * mkdir /srv/jupyterhub
      * cd [/srv/](file:///srv) jupyterhub
      * sudo touch jupyterhub_cookie_secret
      * sudo chown :sudo jupyterhub_cookie_secret
      * sudo chmod g+rw jupyterhub_cookie_secret
      * sudo openssl rand -hex 32 > jupyterhub_cookie_secret
      * sudo chmod 600 jupyterhub_cookie_secret
    * Create proxy auth token
      * cd [/srv/jupyterhub](file:///srv/jupyterhub)
      * sudo touch proxy_auth_token
      * sudo chown :sudo proxy_auth_token
      * sudo chmod g+rw proxy_auth_token
      * sudo openssl rand -hex 32 > proxy_auth_token
      * sudo chmod 600 proxy_auth_token
    * Generate dhparam.pem 
      * cd [/etc/nginx](file:///etc/nginx)
      * sudo touch dhparam.pem
      * sudo chown :sudo dhparam.pem
      * sudo chmod g+rw dhparam.pem
      * sudo openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048
      * sudo chmod 600 dhparam.pem
  * Modify nginx config
    * Modify nginx config or copy role/nginx/nginx.conf
    * Modify /etc/nginx/sites-enabled/default and copy the configuration as in role/nginx/sites-enabled/default (replace with your domain name)
  * Install jupyterhub: <https://jupyterhub.readthedocs.io/en/stable/quickstart.html>
    * Install python 3.5: no greater than 3.5, otherwise it will break nodejs and npm
    * Install pip3: sudo apt install python3-pip
    * Install nodejs: <https://nodejs.org/en/download/package-manager/>
    * Install jupyter notebook: sudo pip3 install jupyter
    * Install jupyterhub
		* sudo python3 -m pip install jupyterhub
		* sudo npm install -g configurable-http-proxy
		* sudo python3 -m pip install notebook
    * Install systemd spawner: <https://github.com/jupyterhub/systemdspawner>
  * Install nbgrader
	* Global install  + assignment list
		* pip3 install nbgrader
		* jupyter serverextension enable --system --py nbgrader
		* jupyter nbextension install --system --py nbgrader --overwrite
		* jupyter nbextension enable --sys-prefix assignment_list/main --section=tree
		* jupyter serverextension enable --sys-prefix nbgrader.server_extensions.assignment_list
		* Extensions
			* pip3 install jupyterlab
			* jupyter labextension install jupyterlab-drawio
			* Contrib
				* pip3 install jupyter_contrib_nbextensions
				* jupyter contrib nbextension install --sys-prefix
				* enable contrib extensions:
					* jupyter nbextension enable --sys-prefix codefolding/main
					* jupyter nbextension enable --sys-prefix nbTranslate/main 
					* jupyter nbextension enable --sys-prefix collapsible_headings/main
			* RISE (presentation)
				a. <ttps://github.com/damianavila/RISE>
	* Instructor only (local)
		* jupyter nbextension enable --user --py nbgrader


Releasing feedback to student assignment directory
=============
* Before releasing feedback, the html files containing the feedback have to be generated with [nb grader](https://nbgrader.readthedocs.io/en/0.2.x/user_guide/06_returning_feedback.html).
```
nbgrader feedback assignment_id
```
* Now, we can send back the feedbacks to student directory
```
sudo config/release_feedback.py --assignment_id WuS-01
```
* Arguments:
  * --assignment_id : specify the assignment id
  * --student_id : create feedback for a specific student
  * --student_group : create feedback for the students in a group (Linux group)
* If there is no student id specified, then it will generate feedback for all students

Generating pdfs from the feedback
=============

