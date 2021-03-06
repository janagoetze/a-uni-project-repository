'''Demo calls for a-uni-project'''

from nlp.processing import NLP
import spacy
import os


def demo():

    print('''
    **********
    1) Creating NLP object
    nlp = NLP()
    ''')
    nlp = NLP()

    print('''
    **********
    2) Data preprocessing
    preprocessed = nlp.preprocess('Alice was beginning to get very tired.')
    ''')
    preprocessed = nlp.preprocess('Alice was beginning to get very tired.')

    print('''
    **********
    3) Data splitting
    train, dev, test = nlp.split_data(preprocessed)
    ''')
    train, dev, test = nlp.split_data(preprocessed)
    print(train, dev, test)

    print('''
    **********
    4) Model building
    my_model = nlp.build_model(train)
    ''')
    my_model = nlp.build_model(train)

    print('''
    **********
    5) Evaluation
    eval_score = nlp.evaluate(my_model, test)
    print(eval_score)
    ''')
    eval_score = nlp.evaluate(my_model, test)
    print(eval_score)


if __name__ == '__main__':
    demo()

    # this should create a folder and file in your local directory
    if not os.path.exists('DATA'):
        os.makedirs('DATA')
    with open('DATA/docker_test.log', 'w') as outfile:
        outfile.write("Let's see if this works as intended.")
