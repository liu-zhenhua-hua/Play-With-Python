#!/Users/tony/anaconda3/bin/python3

"""
To configure the virtual environment, using python standard env module

pip3 list -- to see how many packages has been installed in your system.

1. $python3 -m env project_env    project_env is our virtual env name.
2. $source project_env/bin/activate
3. $which python (with python env you are using )
4. $pip3 list (list of packages for the current python virtual env)
5. $pip3 freeze > requirements.txt. export the packages and version, you can import it at another venv
6. $deactivate
7. $rm -rf project_env/   delete the venv totally.


now we are going to create another venv under my_project folder, please execute the following command

1. $python3 -m venv my_project/venv
2. $source my_project/venv/bin/activate
3. $pip install -r requirements.txt       #import the previous packages list which export from last venv environment.



now we are going to create a new venv environment, with global site packages
1. $python3 -m venv venv --system-site-packages
2. $source /venv/bin/activate
3. $pip list
4. $pip list --local
"""