# django-clean-project
My default django project layout

## Requirements
	- Clone the repository
	- **Will require a virtualenvwrapper setup**
	- Simply create a a virtualenv folder and activate
		`mkvirtualenv project-name`
		`workon project-name`

	- Add environmental variables in postactivate script, directory located: ~/.virtualenvs/project-name/bin/postactivate
		`export DJANGO_SETTINGS_MODULE=config.settings.local`
		`export PYTHONPATH=$PYTHONPATH:$HOME/Project/project-name/config`
		`export LOCAL_SECRET_KEY='DJANGOPASSWORDHERE'
		`export DATABASE_PASSWORD='SETYOURPASSWORDHERE'

	- Pip install requirements
		`pip install -r requirements.txt`

	- Run `127.0.0.1:8000` locally to test it out!
