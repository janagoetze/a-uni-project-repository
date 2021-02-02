'''Example (dummy) code for doing something meaningful'''

from nlp.processing import NLP
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s'
                    )


def main():
    # paths and configurations
    # tip: use click module to parametrize
    DATADIR = 'path/to/data'
    ANALYSIS = 'path/to/write/analysis/to'
    RESULTS = 'path/to/write/results/to'

    nlp = NLP()

    # Reading and processing data
    logging.info('Reading data from {}'.format(DATADIR))
    preprocessed = nlp.preprocess(DATADIR)
    logging.info('NLP analysis written to {}'.format(ANALYSIS))
    train, dev, test = nlp.split_data(preprocessed)

    # Build model and improve using dev set
    my_model = nlp.build_model(train)

    # Evaluate
    eval_score = nlp.evaluate(my_model, test)
    logging.info(eval_score)
    logging.info('Results written to {}'.format(RESULTS))


if __name__ == '__main__':
    main()
