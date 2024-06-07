# cfsc2024-ex-paths

### Summary

This repo is part of an exercise for the Brown University **2024 Computational Fluency Short Course**, for practice with file paths and directory trees.

It is provided for solely educational purposes. Use at your own risk; no express or implied warrantees are given.

### Installation

Running the notebook requires `python` with some dependencies, including Jupyter lab (or at least notebooks). Only minimal dependencies are needed, so it is likely everything would work from the "base" environment of Anaconda. However, best practice is to make a new environment rather than rely on the base across projects.

If you have `conda`, you can create a virtual environment from a shell (terminal) command line (be sure your current working directory is the top of the repo) and open Jupyter with:

```
conda env create -f environment.yml
conda activate cfsc2024-paths
jupyter lab
```

If you are using Anaconda Navigator, you can go to the `Environments` tab, and use the menu options to build from the file `environment.yml`. In order to use the environment, you must select it from the drop down at the top of Navigator **before starting Jupyter Lab** in the GUI.

The main code is the notebook `analyze_reaction_times.ipynb` in the `notebooks` directory. The notebook assumes its working directory is `notebooks`, one level below the top of the repo.

### Additional notes

**(1)**: As discussed in class, generally one keeps data out of git repositories. An exception is a `testdata` folder that contains very small and text based (CSV) data that shows how the code should work. In a larger project, one would typically maintain paths to some data directory outside the repo, or have the code download the data automatically from an online source.

**(2)**: Jupyter notebooks are a little crunchy when used with git. The issue is that git has to track *all* changes in a file, which for a notebook includes both the code you want to track, and also every meaningless update in the outputs (e.g. just rerunning a cell without changing any code looks like a change to git). Moreover, notebooks can contain images and other large data that bloats a git repo.

While there's no universally accepted approach, one common choice is to `Clear all outputs` under the `Edit` menu in Jupyter before adding and committing any code changes. This saves a clean notebook and allows git to focus on code changes, but also means anyone using the notebook will need to be able to run all the cells to see its outputs.

A variation on the idea is to save a PDF version of the notebook, and then clear all outputs before committing. There are also packages that extend git's capabilities to "understand" notebook structure.

### Contributors

Jason Ritt, Brown University
