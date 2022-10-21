### Softwares and Tools Used###

1. [Github Account](https://github.com)
2. [Git CLI](https://git-scm.com/)
3. [VS Code](https://code.visualstudio.com)

Create a virtual environment to specify Python on Visual Studio

    conda create -p venv python==3.7 -y

Criando ambiente virtual para o python no Power Shell:

    py -3 -m venv .venv
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
    .venv\scripts\activate

Criando o arquivo requirements.txt com as principais bibliotecas necessárias em todo projeto:

    sklearn
    pandas
    matplotlib
    numpy
    scipy
    plotly
    schedule
    papermill

ou

    pip3 freeze > requirements.txt

    
Instalando as bibliotecas do python necessárias para o projeto no ambiente virtual:
    pip install -r requirements.txt

Enviando os arquivos para o github:

    git config --global user.name
    git config --global user.email
    git add . 
    git status
    git commit -m "Readme.md, Requirement.txt, dataset..."
    git push origin main

Run app (app_name):

    python app_name.py