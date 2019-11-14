from os import path

from create_db import *
from create_training_data import *
from nmt_chatbot.inference import inference


if __name__ == '__main__':
    create_table_main()

    print('Table created! Creating training data...')
    if path.exists('{}.db'.format(timeframe)):
        create_training_data()

        print('Training data created!')


# this method should be called only when your chatbot training is finished!
def interact():
    print("Hello! Nice to meet you! Enter E to exit")
    while True:
        question = str(input("> "))

        if question == 'E':
            print("Goodbye!")
            return

        if question != '' and question is not None:
            answer = inference(question)
            print(answer['answers'][0])
