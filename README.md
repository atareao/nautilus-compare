
<!-- start project-info -->
<!--
project_title: Nautilus Compare
github_project: https://github.com/atareao/nautilus-compare
license: MIT
icon: None
homepage: https://www.atareao.es/aplicacion/nautilus-compare
license-badge: True
contributors-badge: True
lastcommit-badge: True
codefactor-badge: True
--->

<!-- end project-info -->

<!-- start badges -->

![License MIT](https://img.shields.io/badge/license-MIT-green)
![Contributors](https://img.shields.io/github/contributors-anon/atareao/nautilus-compare)
![Last commit](https://img.shields.io/github/last-commit/atareao/nautilus-compare)
[![CodeFactor](https://www.codefactor.io/repository/github/atareao/nautilus-compare/badge/master)](https://www.codefactor.io/repository/github/atareao/nautilus-compare/overview/master)
<!-- end badges -->

<!-- start description -->
Compare files directly Nautilus, Nemo or Caja using Meld application
<!-- end description -->

<!-- start prerequisites -->
## Prerequisites

* If you install it from PPA don't worry about, becouse all the requirements are included in the package
* If you clone the repository, you need, at least, these dependecies,

Common required dependencies,

```
python3
python3-gi
python3-plumbum
```

For Nautilus you must install following dependencies,

```
python3-nautilus
gir1.2-nautilus-3.0
```
<!-- end prerequisites -->

<!-- start installing -->
## Installing PDF Tools

To install PDF-Tools for every one of the file managers, run next commands
in a teminal (`Ctrl+Alt+T`), depending the file manager of your distro.

### Nautilus

```
sudo add-apt-repository ppa:atareao/nautilus-extensions
sudo apt update
sudo apt install nautilus-pdf-tools
nautilus -q
```

### Nemo

```
sudo add-apt-repository ppa:atareao/nemo-extensions
sudo apt update
sudo apt install nemo-pdf-tools
nemo -q
```

### Caja

```
sudo add-apt-repository ppa:atareao/caja-extensions
sudo apt update
sudo apt install caja-pdf-tools
caja -q
```
<!-- end installing -->

<!-- start using -->

<!-- end using -->

<!-- start contributing -->
## Contributing to Nautilus PDF Tools

To contribute to **Nautilus PDF Tools**, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
<!-- end contributing -->

<!-- start contributors -->
## 👤 Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
<!-- end contributors -->

<!-- start table-contributors -->

<table id="contributors">
	<tr id="info_avatar">
		<td id="atareao" align="center">
			<a href="https://github.com/atareao">
				<img src="https://avatars3.githubusercontent.com/u/298055?v=4" width="100px"/>
			</a>
		</td>
	</tr>
	<tr id="info_name">
		<td id="atareao" align="center">
			<a href="https://github.com/atareao">
				<strong>Lorenzo Carbonell</strong>
			</a>
		</td>
	</tr>
	<tr id="info_commit">
		<td id="atareao" align="center">
			<a href="/commits?author=atareao">
				<span id="role">💻</span>
			</a>
		</td>
	</tr>
</table>
<!-- end table-contributors -->
