youtube-views
==========

### add views in your videos
[![PYTHON](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![SELENIUM](https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=Selenium&logoColor=white)](https://selenium-python.readthedocs.io/)
![WINDOWS](https://img.shields.io/badge/Windows-0078D6?style=flat&logo=windows&logoColor=white)
![LINUX](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
[![CHROME](https://img.shields.io/badge/Google_chrome-4285F4?style=flat&logo=Google-chrome&logoColor=white)](https://www.google.com/intl/fr_fr/chrome/)


# Introduction
_youtube-views_ est un programme coder en [**python**](https://www.python.org/) qui permet d'accelerer le gain de vue. Il utilise les performances de votre machine en utilisant le _multi-threading_ (module [**threaded**](https://pypi.org/project/threaded/)) pour plus de d'efficacité.

![table](./images/table.png)

![logs](./images/logs.png)


# Installation

## Source code
> [**git**](https://git-scm.com/) et [**python3**](https://www.python.org/) et **pip** sont requis pour l'installation

Pour commencer, télechargez le répositorie avec 

`git clone https://github.com/deepcaps/youtube-views.git`


Déplacez-vous dans le répertoire créé puis effectuez cette commande pour installer les modules necessaires

`pip install -r requirements.txt`

> `python3 -m pip install pip` pour installer **pip**


Démarez ensuite le programme avec
> Vous devez avoir la version _96.0.4664.45_ de chrome ou télecharger la version correspondante à votre navigateur chrome [_ici_](https://chromedriver.chromium.org/) et la remplacer par le fichier _chromedriver.exe_ ou _chromedriver_ si ce n'est pas la bonne version (pour connaitre sa version de chrome: [_tuto_](https://assistance.orange.fr/ordinateurs-peripheriques/installer-et-utiliser/la-recherche-et-navigation-sur-le-web-cookies/un-navigateur/google-chrome/google-chrome-verifier-la-version-et-mettre-a-jour_34337-35111))

`python3 bot.py`

![main](./images/main.png)

## Windows executable
> L'executable n'est peut être pas avec la dernière version du bot

Télechargez [_l'executable windows_](https://github.com/deepcaps/youtube-views/releases/download/versions/youtube-views.zip) puis executez le simplement sans installation

> Vous devez avoir la version _96.0.4664.45_ de chrome ou télecharger la version correspondante à votre navigateur chrome [_ici_](https://chromedriver.chromium.org/) et la remplacer par le fichier _chromedriver.exe_ (pour connaitre sa version de chrome: [_tuto_](https://assistance.orange.fr/ordinateurs-peripheriques/installer-et-utiliser/la-recherche-et-navigation-sur-le-web-cookies/un-navigateur/google-chrome/google-chrome-verifier-la-version-et-mettre-a-jour_34337-35111))

![executable](./images/executable.png)

Vous devriez peut être avoir besoin de **débloquer** l'application avant de l'executer. Pour cela:
- Clic-droit => _propriétées_ sur le fichier
- Cocher la case _débloquer_

![unblock](./images/unblock.png)

> Si le bot ne fonctionne toujours pas, désactivez [_windows defender_](https://support.microsoft.com/en-us/windows/turn-off-defender-antivirus-protection-in-windows-security-99e6004f-c54c-8509-773c-a4d776b77960) puis relancer le programme.


# How to use

Après avoir installé et lancé le bot (voir [Installation](#installation)), appuyez sur `[ENTER]` pour le démarer

![main](./images/main.png)

Pour la première options (_link of the video_), vous devez simplement entrer le lien de la vidéo qui va être ciblée.

![link](./images/link.png)

Ensuite, pour la deuxième options (_watch time_), vous devez indiquez le temps que le bot restera sur la vidéo **en secondes**.
> Plus le bot reste longtemps, plus la vidéo sera référencé

![watchTime](./images/watchTime.png)

Pour la troisième option (_thread nbr_), vous devez entrer **un entier** qui correspondra au nombre de session lancé simultanément. Plus le chiffre est élevé, plus il y aura de vues rapidement mais plus cela utilisera de la **RAM**.
> La valeur recommendée est **5** pour un pc moyen (8 go de RAM) mais cela dépend de votre utilisation et de vos performances.

![threadNbr](./images/threadNbr.png)

Pour finir, pour la dernière option (_repetion nbr_), vous devez indiquer le nombre de boucle que va faire le programme. Cette options n'utilise pas de performances supplémentaires contrairement à _thread nbr_
> Vous pouvez terminer le programme avant la fin des répétitions avec le racourcie _CTRL + C_

![rep](./images/rep.png)

Le programme effectura un **test de connexion** sur l'hote _www.youtube.com_ et vous calculera ensuite une estimation des vues que cela vous rapporteras et du temps que cela va prendre.
> Le temps peut varier en fonction des **performances** de votre machine et de l'évolution de votre **vitesse de connexion**

![table](./images/table.png)


# To know
Le projet est un bot créé par **@deepcaps** avec [selenium](https://selenium-python.readthedocs.io/).

Aucune donnés n'est enregistrées.

Les librairies utilisées sont:
- colorama
- selenium
- platform
- time
- threaded
- os
- pystyle


# Me contacter
Vous pouvez me contacter a l'adresse [**deepcaps@outlook.com**](deepcaps@outlook.com) pour me faire parvenir les bugs ou les fonctionnalités à rajouter.


# Infos
![MAINTENED](https://img.shields.io/badge/maintained-yes-green.svg)

![infos](https://github-readme-streak-stats.herokuapp.com/?user=deepcaps)
