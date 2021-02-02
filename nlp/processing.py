import random

class NLP:
    '''Dummy class for some natural language processing'''

    def __init__(self):
        self.tokenizer = None  # custom tokenization

    def preprocess(self, text):
        '''Method that processes the data'''
        print('Tokenizing...')
        print('Lemmatizing...')
        print('Fancy processing...')
        return 'Processed text'

    def build_model(self, preprocessed_data):
        print('Building model...')
        return 'A model for solving some very difficult task'

    def evaluate(self, model, test_data):
        print('Evaluating the model against some test data...')
        return random.random()

    @staticmethod
    def split_data(data):
        train, dev, test = '70%', '10%', '20%'
        return train, dev, test
