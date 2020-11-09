# Documenting Instructions

## Installation

### Install Conda

You can install [Anaconda](https://docs.anaconda.com/anaconda/install/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to install conda package manager (if you don't know the difference you should install anaconda).

### Create documentation environment

Now we need to create the appropriate environment for documenting by installing all the necessary tools. To do so we have provided you an environment droplet, which is a recipe for a series of installations that create the aforementioned environment. For that, after directing to the root folder of this project where the environment droplet (`environment.yml`) is located, you need to run the following command:

``` shell
conda env create -f environment.yml
```

---

## Start Work on Documentation

After finishing your work on documentation you need to shutdown the server and deactivate the environment.

### Activate the Environment

Now that you have created the appropriate environment, you need to activate the environment to be able to work inside it. For that, as you are in the root folder of this project, you need to run the following command:

``` shell
conda activate spatial_computing_docs
```

If the command line is now indicating the name of the environment in paranthesis, it means that the environment is activated. Similar to this

``` shell
(spatial_computing_docs) {your username}@{your computer name} spatial_computing_project_template %
```

### Run the Local Server

Now that the environment is activated, we need to run the local server to be able to see the result of changes in the local version of the documentation website. For that, run the following command:

``` shell
mkdocs serve
```

After running this command, if the server has started to work successfully, you should see the following line in the command line:

``` shell
INFO    -  Serving on http://127.0.0.1:8000
```

This means that the server is accessible at `http://127.0.0.1:8000`. If you open your browser and go this link you should see a local version of the site.

---

## Writing Your Documentation

In the documenting process you need to head to the `docs` folder and edit the `.md` (markdown) files, since the website is build from these files.

In the root of this project, you can edit the configurations of your project in `mkdocs.yml` file:

* Adding o removing [pages](https://www.mkdocs.org/user-guide/writing-your-docs/)
* Add [markdown extensions](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/). Some of the useful extensions:
    * [arithmatex](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/) for writing mathematics
    * [highlight](https://facelessuser.github.io/pymdown-extensions/extensions/highlight/) for code highlighting
* [Customizing](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/) the looks of your documentation
* Adding [MkDocs Plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins), such as:
    * [mknotebooks](https://github.com/greenape/mknotebooks) for including python notebooks in the documentations

---

## Finish Work on Documentation

### Server Shut Down

To shutdown the server, you need to press ++ctrl+c++ in the command line. The following should appear in the command line:

``` shell
INFO    -  Shutting down...
```

### Deactivate Environment

After shutting down your server the command line is back to the normal state and you can run commands again. To deactivate your environment you need to run the following command:

``` shell
conda deactivate
```

---

## Deployment of the Documentation Site

### Build and Deploy

to deploy your documentation website, you need to run the following command in the root of this repository:

``` shell
mkdocs gh-deploy
```

This command will create a new branch in your repository called `gh-pages` and build your site in it. It will then push the new branch to your remote repository automatically. It will also create a `site` folder in your root directory containing all of your site files. Since this folder is added `.gitignore` file, it won't be committed or pushed to the remote repository.

### Setup GitHub Pages

For the first time, you need to configure the GitHub Pages service on your GitHub repository so it wil automatically build your documentation website whenever you deploy your site. To do this:

1. Go to your repository setting,
2. got GitHub Pages section,
3. select `gh-pages` branch,
4. select `/(root)` location,
5. click on the `save` button.

The setting page will refresh, and now if you go to the address that is provided at the GitHub Pages section, Wola, here is your documentation! :rocket:
