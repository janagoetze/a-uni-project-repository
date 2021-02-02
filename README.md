# a-uni-project-repository

This is an example git repository that demonstrates the usage of a Dockerfile to submit alongside the Python source code for homework assignments.

## Homework submission

- Course name: "Best course ever"
- Course code: "CL-ABCDE"
- Homework assignment: "Run some NLP analysis on the XYZ data"
- Any other details such a s task variant etc. If your name is not obvious to deduct from your github username, make sure your teacher can identify you.

## Installing / Getting started

Explain what needs to be installed to run the code, such as Python libraries or a language model. For example:

In order to run the code, you need to run the following installation:

```shell
python3.8 -m venv env && . env/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

This creates and activates a virtual environment, installs the necessary Python modules and downloads the necessary spacy model for English.

You can run the demo code by typing:
```shell
python demo.py
```

### Running the Docker container

If you have created a Docker container for your submission, give details here on how to pull and start it and specify what will happen. For example:

The following commandline instructions will pull and start the corresponding Docker container.
```shell
docker pull janagoetze/a-uni-project:example
docker run -it --rm janagoetze/a-uni-project:example
```

This will open a shell environment in which the code can be run as follows:
```shell
python demo.py
python main.py
```
