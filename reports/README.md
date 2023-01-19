---
layout: default
nav_exclude: true
---

# Exam template for 02476 Machine Learning Operations

This is the report template for the exam. Please only remove the text formatted as with three dashes in front and behind
like:

```--- question 1 fill here ---```

where you instead should add your answers. Any other changes may have unwanted consequences when your report is auto
generated in the end of the course. For questions where you are asked to include images, start by adding the image to
the `figures` subfolder (please only use `.png`, `.jpg` or `.jpeg`) and then add the following code in your answer:

```markdown
![my_image](figures/<image>.<extension>)
```

In addition to this markdown file, we also provide the `report.py` script that provides two utility functions:

Running:

```bash
python report.py html
```

will generate an `.html` page of your report. After deadline for answering this template, we will autoscrape
everything in this `reports` folder and then use this utility to generate an `.html` page that will be your serve
as your final handin.

Running

```bash
python report.py check
```

will check your answers in this template against the constrains listed for each question e.g. is your answer too
short, too long, have you included an image when asked to.

For both functions to work it is important that you do not rename anything. The script have two dependencies that can
be installed with `pip install click markdown`.

## Group information

### Question 1
> **Enter the group number you signed up on <learn.inside.dtu.dk>**
>
> Answer:

14

### Question 2
> **Enter the study number for each member in the group**
>
> Example:
>
> *sXXXXXX, sXXXXXX, sXXXXXX*
>
> Answer:

s183910, s183898, s222955, s183912

### Question 3
> **What framework did you choose to work with and did it help you complete the project?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our project. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

From the Pytorch ecosystem we used one of the Pytorch Image models named MobileNet-V2.

We have used the OpenCV for python to showcase the deployed model, and live demonstarte the models translation of a hand guesture into the corresponding letter. Additionally, we have used the request package in python to create the posts instead of using curl.

## Coding environment

> In the following section we are interested in learning more about you local development environment.

### Question 4

> **Explain how you managed dependencies in your project? Explain the process a new team member would have to go**
> **through to get an exact copy of your environment.**
>
> Answer length: 100-200 words
>
> Example:
> *We used ... for managing our dependencies. The list of dependencies was auto-generated using ... . To get a*
> *complete copy of our development enviroment, one would have to run the following commands*
>
> Answer:

We used `pipreqs` for generating a dependency list with exact versions.
Development libraries, such as `pytest` were manually maintained in `requirements.txt`.
To get a complete copy of our development environment one would only have to run the `make requirements` command in the python environment of their choice (provided both python and make are already installed).

To obtain the input data one would have to execute the `make data` command which pulls from a dvc remote.

To locally create the training and prediction environments a new team member would have to build the docker images using `docker build -f predict.dockerfile . -t predict:latest` for inference and `docker build -f train.dockerfile . -t train:latest`, or simply `make build-docker-train` and `make build-docker-predict`.

### Question 5

> **We expect that you initialized your project using the cookiecutter template. Explain the overall structure of your**
> **code. Did you fill out every folder or only a subset?**
>
> Answer length: 100-200 words
>
> Example:
> *From the cookiecutter template we have filled out the ... , ... and ... folder. We have removed the ... folder*
> *because we did not use any ... in our project. We have added an ... folder that contains ... for running our*
> *experiments.*
> Answer:

The project is structured using the cookiecutter data science template.
We filled in `predict_model.py` and `train_model.py`, and we added some extra utility files, e.g. `src/data/__init__.py`, which builds the dataset.
We did not fill in `make_dataset.py`, as the the data requires little preprocessing, which is done at runtime, hence the folders `interim`, `processed`, and `external` is not used. These folders are therefore deleted.

We have added the folder `tests` which contains our tests of data and the model. We have also added the folder `outputs` which is created by running the `train_model.py`. This folder contains the outputs of hydra which saves the logs and cofigurationfiles, to document how the training went and what hyperparameters were used.

We have also added multiple dockerfiles in relation to the build of docker images and containers with all the dependensies required to run specific parts of our project. DVC-files and a DVC-folder are also added to manage the large amount of data in the cloud.

The folder `wandb` has also been added to manage the hyperparameters and do the main visualizations.

### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
>
> Answer:

To ensure code similarity, we used the `black` autoformatter, the `isort` utility and the `flake8` linter with slightly altered configurations. These rules were enforced with a pre-commit git hook that made sure no one would forget to use them (see `.pre-commit-config.yaml`).

Good formatting and code quality improves readability, making it easier for all team members to understand and alter parts of the implementation later. In large projects this is especially important since they change a lot over time and many people contribute to them. Without enforced formatting rules the code would quickly become difficult to maintain.

## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement?**
>
> Answer:

We implemented six unit tests for a coverage of 23 %, focusing mainly on the data and model.
Notable, the training loop and prediction were not covered, as these are larger, self-contained blocks of code where writing unit tests is both harder and provide less benefit over testing stand-alone functions.

### Question 8

> **What is the total code coverage (in percentage) of your code? If you code had an code coverage of 100% (or close**
> **to), would you still trust it to be error free? Explain you reasoning.**
>
> **Answer length: 100-200 words.**
>
> Example:
> *The total code coverage of code is X%, which includes all our source code. We are far from 100% coverage of our **
> *code and even if we were then...*
>
> Answer:

The code coverage is 23 %.
This is not much, but does cover the central parts which are data loading and inference.
This is far from 100 % code coverage.
However, 100 % code average should not be the end all, be all goal, as this does not guarantee code correctness.
It only measures if the code at any point has been run, and tests will rarely cover every input value a piece of code could receive, leading to edge cases not necessarily being discovered even under 100 % coverege.
Further, near 100 % unit test coverage does not guarantee that every part plays nicely together, even if they work individually.

### Question 9

> **Did you workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of both branches and PRs in our project. In our group, each member had an branch that they worked on in*
> *addition to the main branch. To merge code we ...*
>
> Answer:

We made use of both branches and pull requests during our project work. We created new branches as we needed them for testing and implementing specific features, followed by creating a pull request for merging the feature branch into the main branch, once the new feature was complete. Hence, we have had a branch for concerning the replacement of model, the implementing of live demo functions in API, for the implementing of pre-commit features and many more. Our practice regarding the pull requests was to always have another group member doing the approving of it. This was done for the sake of practice and for collaboration.

### Question 10

> **Did you use DVC for managing data in your project? If yes, then how did it improve your project to have version**
> **control of your data. If no, explain a case where it would be beneficial to have version control of your data.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did make use of DVC in the following way: ... . In the end it helped us in ... for controlling ... part of our*
> *pipeline*
>
> Answer:

As an initial resolution, we stored the data on Google Drive and used DVC to manage it. With later improvements, we moved the data to the Data Storage buckets in Google Cloud storage, and continued managing it with DVC.This allowed us to change the data if needed without losing history, and it prevented the impracticalities of saving large amounts of data to a git repository.
It also allowed us to make sure that everyone had the same data laid out in the same way, which was also useful for pipelines and deployment.

### Question 11

> **Discuss you continues integration setup. What kind of CI are you running (unittesting, linting, etc.)? Do you test**
> **multiple operating systems, python version etc. Do you make use of caching? Feel free to insert a link to one of**
> **your github actions workflow.**
>
> Answer length: 200-300 words.
>
> Example:
> *We have organized our CI into 3 separate files: one for doing ..., one for running ... testing and one for running*
> *... . In particular for our ..., we used ... .An example of a triggered workflow can be seen here: <weblink>*
>
> Answer:

We used Github Actions to implement our continuous integration.
Specifically, it consists of linting with `flake8` and unit testing with `pytest`.
This helps ensure that new merge requests follow the code standards and don't break existing functionality.
As we do not have any platform dependant code, we did not run the pipeline over multiple systems, but we did require both steps to succeed.
Further, as the steps in the pipeline where rather simple, we found it best to keep them in a single flow, which not only meant
we only had to have a single file, but it also reduced runtime by not having to set up twice.
A finished workflow can be seen <a href="https://github.com/s183910/MLOps_project/actions/runs/3955272588">here</a>.

## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run a experiment.**
>
> Answer length: 50-100 words.
>
> Example:
> *We used a simple argparser, that worked in the following way: python my_script.py --lr 1e-3 --batch_size 25*
>
> Answer:

We used hydra for controlling hyperparameters, as it allows for config files that help control which experiments were run and makes sure that the correct experiments are run.

### Question 13

> **Reproducibility of experiments are important. Related to the last question, how did you secure that no information**
> **is lost when running experiments and that your experiments are reproducible?**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of config files. Whenever an experiment is run the following happens: ... . To reproduce an experiment*
> *one would have to do ...*
>
> Answer:

Config files are one part of the ansewr, making sure that there is no doubt on the hyperparameters.
DVC also enables us to ensure that the data would be identical from machine to machine, and Docker allowed us to provide a controlled environment with guaranteed library versions, making sure that no changed behaviour in different libraries would have an effect.
The only non-reproducibility comes from stochistic processes such as batch shuffling, which we did not control with seeds.
Even with seeds, PyTorch does not guarantee exactly the same outputs.

### Question 14

> **Upload 1 to 3 screenshots that show the experiments that you have done in W&B (or another experiment tracking**
> **service of your choice). This may include loss graphs, logged images, hyperparameter sweeps etc. You can take**
> **inspiration from [this figure](figures/wandb.png). Explain what metrics you are tracking and why they are**
> **important.**
>
> Answer length: 200-300 words + 1 to 3 screenshots.
>
> Example:
> *As seen in the first image when have tracked ... and ... which both inform us about ... in our experiments.*
> *As seen in the second image we are also tracking ... and ...*
>
> Answer:

The first figure shows a simple training loss curved tracked in Weights & Biases.
This is one of the most important metrics to track during training, both to inform us about training stability and overfitting in tandem with the validation loss.
The second figure shows how Weights & Biases was uses to track different experiments, where we could filter by hyperparameter choices and other variables.
This is one way to overcome the classical problem of accidentally overriding previous experiments or messing up which were which.

### Question 15

> **Docker is an important tool for creating containerized applications. Explain how you used docker in your**
> **experiments? Include how you would run your docker images and include a link to one of your docker files.**
>
> Answer length: 100-200 words.
>
> Example:
> *For our project we developed several images: one for training, inference and deployment. For example to run the*
> *training docker image: `docker run trainer:latest lr=1e-3 batch_size=64`. Link to docker file: <weblink>*
>
> Answer:

We build three docker images: `predict.dockerfile` for doing inference, `trainer.dockerfile` for training, and `api/gcp_run/dockerfile` for deploying to GCP.
The two first primarily differ in their entry points, with one starting training and the other evaluation.
The final is quite different, as it does not have an entry point, but instead uses `CMD` to start the inference api.

### Question 16

> **When running into bugs while trying to run your experiments, how did you perform debugging? Additionally, did you**
> **try to profile your code or do you think it is already perfect?**
>
> Answer length: 100-200 words.
>
> Example:
> *Debugging method was dependent on group member. Some just used ... and others used ... . We did a single profiling*
> *run of our main code at some point that showed ...*
>
> Answer:

We did not enforce debugging practices, as we found this was best left to individual preferences and circumstances.
The debugging methods used ranged from VS Code's built-in debugger to the IPython debugger (`ipdb`) to the never-failing `print` spam.
We profiled our code after we got the main flows working to make sure that we were satisfied with the runtime, mainly that the bottlenecks were the neural networks as would be expected.

## Working in the cloud

> In the following section we would like to know more about your experience when developing in the cloud.

### Question 17

> **List all the GCP services that you made use of in your project and shortly explain what each service does?**
>
> Answer length: 50-200 words.
>
> Example:
> *We used the following two services: Engine and Bucket. Engine is used for... and Bucket is used for...*
>
> Answer:

<!-- TODO finish this -->
We made use of the following services on google cloud platform:
- Buckets for storing Docker images and data storage
- Cloud Run for building the inference API
- Cloud Functions for the same TODO???

### Question 18

> **The backbone of GCP is the Compute engine. Explained how you made use of this service and what type of VMs**
> **you used?**
>
> Answer length: 50-100 words.
>
> Example:
> *We used the compute engine to run our ... . We used instances with the following hardware: ... and we started the*
> *using a custom container: ...*
>
> Answer:

--- question 18 fill here ---

### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

--- question 19 fill here ---

### Question 20

> **Upload one image of your GCP container registry, such that we can see the different images that you have stored.**
> **You can take inspiration from [this figure](figures/registry.png).**
>
> Answer:

--- question 20 fill here ---

### Question 21

> **Upload one image of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:

--- question 21 fill here ---

### Question 22

> **Did you manage to deploy your model, either in locally or cloud? If not, describe why. If yes, describe how and**
> **preferably how you invoke your deployed service?**
>
> Answer length: 100-200 words.
>
> Example:
> *For deployment we wrapped our model into application using ... . We first tried locally serving the model, which*
> *worked. Afterwards we deployed it in the cloud, using ... . To invoke the service an user would call*
> *`curl -X POST -F "file=@file.json"<weburl>`*
>
> Answer:

--- question 22 fill here ---

### Question 23

> **Did you manage to implement monitoring of your deployed model? If yes, explain how it works. If not, explain how**
> **monitoring would help the longevity of your application.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could*
> *measure ... and ... that would inform us about this ... behaviour of our application.*
>
> Answer:

--- question 23 fill here ---

### Question 24

> **How many credits did you end up using during the project and what service was most expensive?**
>
> Answer length: 25-100 words.
>
> Example:
> *Group member 1 used ..., Group member 2 used ..., in total ... credits was spend during development. The service*
> *costing the most was ... due to ...*
>
> Answer:

--- question 24 fill here ---

## Overall discussion of project

> In the following section we would like you to think about the general structure of your project.

### Question 25

> **Include a figure that describes the overall architecture of your system and what services that you make use of.**
> **You can take inspiration from [this figure](figures/overview.png). Additionally in your own words, explain the**
> **overall steps in figure.**
>
> Answer length: 200-400 words
>
> Example:
> *
> *The starting point of the diagram is our local setup, where we integrated ... and ... and ... into our code.*
> *Whenever we commit code and puch to github, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:

--- question 25 fill here ---

### Question 26

> **Discuss the overall struggles of the project. Where did you spend most time and what did you do to overcome these**
> **challenges?**
>
> Answer length: 200-400 words.
>
> Example:
> *The biggest challenges in the project was using ... tool to do ... . The reason for this was ...*
>
> Answer:

--- question 26 fill here ---

### Question 27

> **State the individual contributions of each team member. This is required information from DTU, because we need to**
> **make sure all members contributed actively to the project**
>
> Answer length: 50-200 words.
>
> Example:
> *Student sXXXXXX was in charge of developing of setting up the initial cookie cutter project and developing of the*
> *docker containers for training our applications.*
> *Student sXXXXXX was in charge of training our models in the cloud and deploying them afterwards.*
> *All members contributed to code by...*
>
> Answer:

--- question 27 fill here ---
