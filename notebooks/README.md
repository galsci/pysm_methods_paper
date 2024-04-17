# Notebooks to generate figures

This folder should be used to store notebooks used to generate figures in the paper.

Some recommendations:

* Import all packages at the top of the notebook to highlight all dependencies together
* If you use data please use `wget` inside the notebook to retrieve them at execution time or assume that the notebook is being executed on `Jupyter@NERSC` and point to paths on Perlmutter accessible by the `cmb` group
* Write the updated figures directly inside the `../figures` folder
* Do not store outputs inside the Notebooks, it is best to clean them up with `nbstripout` before uploading them