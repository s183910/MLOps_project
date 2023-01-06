# MLOps project - Hand Gesture Recognition
<!-- ============================== -->

Katrine Bay s183910

Rasmus Bryld s183898

Asger Schultz s183912

Eper Stinner s222955


## Main goal of the project

The objective of this project is to develop a Convolutional Neural Network (CNN) capable of transcribing static hand gestures in American Sign Language (ASL) into the corresponding English alphabet letters. Additionally, if feasible, the network will be enhanced to classify dynamic hand movement sequences to translate signs representing words. The potential for converting the images to 3D hand landmarks using MediaPipe, before classification, will also be explored.

## Frameworks expected to be implemented

- Which: We expect to be using PyTorch and/or Tensorflow. Potentially, the framework MediaPipe will be applied.
<!-- - How: We intend to utilise a pretrained model from the Transformer framework, as we will focus on creating a well organised, reproducable, scalable and xx project repository. -->
- How: We intend to utilise a rather simple CNN, as we will focus on creating a well organised, reproducable, scalable and xx project repository.

## Data

The data set which will be used in this project is the [Sign Language MNIST](https://www.kaggle.com/datasets/datamunge/sign-language-mnist) data set on Kaggle licensed under [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/). TODO here we will write about the data - look in the overleaf.

If we consider it a viable option, will also look for a data set with 3D hand joint coordinates and matching hand gestures. If no data sets are available, we can create our own, or convert existing images to hand joints using MediaPipe under the assumption that MediaPipe can accurately estimate the hand joints.


## Deep learning models
TODO:
Due to the time limitations on the project, we make use of pre-trained models. We will implement xxx and xxx and compare the results of the gesture recognition
\\

If we manage to work with hand landmarks instead of images with the help of MediaPipe, it will likely be possible to get good performance with very shallow neural networks, considering the low dimensionality of the data (21 landmarks x 3 coordinates). Simpler baselines like Random Forest (RF) might also work well.




Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
