# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

kg="rupa"
r=["1","2","3","4"]
print(" ".join(r))
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter

import spacy
nlp=spacy.load('en')
doc=nlp('Can you find me flights to Bangalore from Kolkata on 17th of October')
for ent in doc.ents:
    print(ent.text+" "+ent.label_)
    if(ent.label_=='DATE'):
        print(ent.text)  #Universal date formatting required!
        



import re

matchs=re.search('(to|in) ([A-z]+){1}','Tour in Europe ')
#matchs=re.search('from ([A-z]+){1}','Travel to Bangalore ')

if matchs is not None:
    print(matchs.group())
else:
    print(':p')
    
    

args={"pipeline" : [ "nlp_spacy",
                   "tokenizer_spacy",
                    "ner_crf",
                    "ner_spacy",
                    "intent_featurizer_spacy",
                    "intent_classifier_sklearn"]}


training_data = load_data('training_data.json')
configuration = RasaNLUConfig(cmdline_args = args)
trainer = Trainer(configuration)

interpreter=trainer.train(training_data)
query_string='Get me trains to Kerala on 7th of July'
parsed_data=interpreter.parse(query_string)
#print(parsed_data)
entities=parsed_data['entities']
for ent in entities:
    print(ent['entity']+"  "+ent['value'])
    
import sys
import random
cur_state=None
"INIT"=0;
"ENQUIRE"=1;
"END"=2;

INIT_response=['Ask a question!','How may I help you?','Anything I can do for you?']
ENQUIRE_response_travel=['Yes go to Home, then go to Choices, then select date as {} and enter destination as {}']
ENQUIRE_response_hospitality=['Ask a question!','How may I help you?','Anything I can do for you?']
ENQUIRE_response_itinerary=['Ask a question!','How may I help you?','Anything I can do for you?']


args={"pipeline" : [ "nlp_spacy",
                   "tokenizer_spacy",
                    "ner_crf",
                    "ner_spacy",
                    "intent_featurizer_spacy",
                    "intent_classifier_sklearn"]}
    
    
policy={(None, "INIT"):("INIT")}

training_data = load_data('training_data.json')
configuration = RasaNLUConfig(cmdline_args = args)
trainer = Trainer(configuration)

interpreter=trainer.train(training_data)


def getResponse(entities=None):
    if cur_state in "INIT":
        return random.choice(INIT_response)
    if cur_state in "ENQUIRE":
    
    if cur_state in "END":
        

def processResponse(user_text):
    response_data=interpreter.parse(user_text)    
    cur_state=response_data['intent']
    getResponse()
    
def carry_user():
    user=(input('BOT: Type hi! to start : \n')).strip('\n')
    if 'end' in user:
        print('here')
        sys.exit(0)
    getResponse(user)    

try:
    while True:
        carry_user()
except KeyboardInterrupt:
    pass


user=input('BOT: Type hi! to start')
print(random.choice(INIT_response))

r={'1':1,'2':2}

if r.get('3',None) is None:
    print('here')
    






