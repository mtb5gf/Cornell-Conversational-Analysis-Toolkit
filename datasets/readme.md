**A.)** This dataset is taken from the Emory Character Mining Dataset. It contains annotated scripts of all ten seasons of the popular 1990s sitcom _Friends_. The Emory NLP Group has published several papers in recent years:

* [Character Identification](../../../character-identification) (since May 2016).
* [Emotion Detection](../../../emotion-detection) (since May 2017).
* [Reading Comprehension](../../../reading-comprehension) (since May 2018).
* [Questiong Answering](../../../question-answering) (since May 2019).

While these projects focus largely on determining characteristics generated in utterances, this adaptation into Convokit is largely focused on how User-Level patterns of utterance affect a narrative's ability to delineate major and minor characters.  

**B1.) User-Level**
_character_name_: Contains the full name of the character/user 
_total_utterances_: Contains the number of utterances made by the character/user during the entirety of _Friends_
_utterances_per_season_: Contains the number of utterances each character/user makes during a season of _Friends_
_total_references_: Contains the number of references made to the character/user during the first four seasons of _Friends_
_references_per_season_: Contains the number of references each character/user makes during the first four seasons of _Friends_

**B2.) Utterance_Level**
_id_: Contains information about the season, episode, and scene the utterance occurs
_root_: Contains the first utterance within a scene
_text_: Contains the string made in the utterance.
_user_: Identifies the character making the utterance
_meta_: Additional metadata
_reply_to_: Identifies the character/user the user/character of the utterance is referring to. Null if first conversation in scene
_timestamp_: Time the utterance occurs (Not featured in this conversion)

**B3.) Conversation_Level**
Contains the _id_ of the conversations/scenes that occur in the series

**C.) Corpus Stats**
Number of Users: 699
Number of Utterances: 67373
Number of Conversations: 3107
**D.) Contact**
Corpus Created By: Malcolm Bare