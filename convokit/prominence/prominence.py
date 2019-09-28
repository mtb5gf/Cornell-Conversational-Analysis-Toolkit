from convokit.model import Corpus, User
from convokit.transformer import Transformer
import random
import numpy as np
from collections import Counter

class Prominence(Transformer):
	
	def __init__(self):
		pass 
	
	#tranforms#
	def transform(self, corpus: Corpus):
		for character in corpus.get_usernames():
			user1 = corpus.get_user(character)
			utterances = user1.get_utterance_ids()
			utterances_per_conversation =[]
			conversations = []
			for uid in utterances:
				utterance = corpus.get_utterance(uid)
				conversation = corpus.get_conversation(utterance.root)
				conversations.append(utterance.root)
				utterances_per_conversation.append((utterance.root, len(conversation.get_usernames()), len(conversation.get_utterance_ids())))
				first_last = 0
				if uid in (utterance.root, list(conversation.get_utterance_ids())[-1]): 
					first_last +=1
			raw_count = len(utterances)/len(list(corpus.utterances.values()))
			total_conversations = len(set(conversations))
			#bootstrapping
			iterations = 0
			for i in range(20):
				samples = random.choices(utterances, k=25)
				#for politeness complexity#
				politeness_rows = []
				#many operations#
				for uid in samples:
					politeness_rows.append(list(corpus.get_utterance(uid).meta["politeness_strategies"].values()))			
			#politeness#
				politeness_results = np.sum(politeness_rows, 0)
				politeness_results_count = len([i/len(politeness_rows) for i in politeness_results if i != 0.0])/len(politeness_rows)
				iterations += politeness_results_count
			#politness_final#
			politeness_final = iterations/20
			#first/last#
			first_last_count = first_last/total_conversations
			#utterances_per_conversation#
			utterances_per_conversations = Counter(utterances_per_conversation)
			upc_final = []
			for k, v in utterances_per_conversations.items():
				average = k[2]/k[1]
				upc_final.append(v/average)
			upc_count = sum(upc_final)/len(utterances_per_conversations)
			user1.add_meta('politeness_complexity', politeness_final)
			user1.add_meta('utterance_per_conversation', upc_count)
			user1.add_meta('first_last_word', first_last_count)
			user1.add_meta('raw_count', raw_count)
		return(corpus)
