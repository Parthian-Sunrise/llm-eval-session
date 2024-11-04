# llm-eval-session
Repo for the LLM eval session

# Dev Set-Up

## 1: Clone Repo
This repo is designed to be edited in WSL, to avoid line-ending issues apply the following git config:
```
git config --global core.autocrlf false
```

## 2: Environment Set-Up
Navigate to the project folder i.e.
```
cd ~/projects/llm-eval-session
```
Once in the repo folder, create a virtual environment using python3-venv for Python 3.12.5 i.e. 
```
python3 -m venv venv
```
Once the environment is initialised, activate it using:
```
source venv/bin/activate
```
When opening the repo in the future activate the venv using the above command or add the following line to your .bashrc (it activates the command if a venv subdirectory is detected)
```
cd() { builtin cd "$@" && [ -d venv ] && source venv/bin/activate; }
```
Next install the requirements:
- developer_requirements.txt: This should include all packages required to edit the repo (packages the end user doesn't require)
- requirements.txt: This should include all packages required to run any notebooks or scripts in the repo itself 

To do this run:
```pip3 install -r requirements.txt```

## 3: Activate pre-commit hooks
Check your .pre-commit-config file is present, then run the following
```
pre-commit install
```


