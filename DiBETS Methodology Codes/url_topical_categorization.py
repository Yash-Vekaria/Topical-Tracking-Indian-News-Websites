import gensim, nltk, os
from urllib.parse import urlparse
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from numpy import dot
from numpy.linalg import norm
import pandas as pd

topic_dictionary = {}
topic_head_embeddings = {}
topic_total_embeddings = {}

# This mapping was pre-created separately before running this code using the function : google_translate_hindi_to_english()
hindi_to_english_mapping = {
	'dailyrashiphal': 'daily horoscope', 'rashiphal': 'horoscope', 'raashiphal': 'horoscope', 'dailyraashiphal': 'daily horoscope', 'daily-rashiphal': 'daily horoscope', 
	'daily-raashiphal': 'daily-horoscope', 'rashifal': 'horoscope', 'raashifal': 'horoscope', 'dailyraashifal': 'daily horoscope', 'daily-raashifal': 'daily-horoscope', 
	'jigyasa': 'curiosity', 'jigyaasa': 'curiosity', 'rashi': 'amount', 'raashi': 'amount', 'aapketaren': 'operators', 'aap-ke-tarein': 'the stars', 'aap-ke-taren': 'you-train', 
	'aap-ke-taarein': 'the stars', 'aapketaarein': 'Your ways', 'aapketarein': 'Operators', 'tauras': 'taurus', 'sagitarrius': 'sagittarius', 'jurm': 'crime', 
	'sahitya': 'literature', 'samiksha': 'review', 'sahitya-samiksha': 'literature reviews', 'sahitya-behes': 'literature', 'arti': 'arti', 
	'sahitya-interview': 'literature interview', 'dharm': 'religion', 'kavya': 'poetry', 'shakti': 'power', 'tarein': 'the stars', 'dharma-karma': 'religion', 'karm': 'karma', 
	'mandir': 'temple', 'pooja': 'prayer', 'pooja-path': 'path of worship', 'dharma': 'religion', 'social-responsibility': 'social responsibility', 'jyotish': 'astrology', 
	'panchang': 'almanac', 'bhajan': 'hymn', 'taren': 'the stars', 'mantra-bhajan-arti': 'mantra-bhajan-aarti', 'dharmik': 'religious', 'dharmik-sthal': 'religious place', 
	'sthal': 'the site', 'daily-scorpion': 'daily-scorpio', 'darshan': 'visit', 'techonology-science': 'technology-science', 'bazaar': 'market', 'bazar': 'market', 
	'management-mantra': 'management mantra', 'khana': 'food', 'khana-khazana': 'food treasure', 'jeevan-mantra': 'life mantra', 'jeevan': 'life', 'pravasi': 'migrant', 
	'hindi-film': 'hindi movie', 'karyakrams': 'event:', 'karyakram': 'program', 'khazana': 'treasure', 'manoranjan': 'entertainment', 'vardaat': 'the incident', 
	'dangal': 'the riot', 'saas-bahu': 'mother in law, daughter in law', 'saas': 'mother in law', 'bahu': 'daughter in law'
}

# This mapping was created by human expert based on which keywords of the topical dictionary might be representative of the main topical subpage for each topic
primary_topic_page = {
	'Art, Culture and Society': ['art', 'culture', 'social', 'society', 'astrology', 'horoscope', 'religion', 'religion-news', 'literature', 'sahitya', 'india-culture', 'indian-culture', 'history-and-culture', 'india-history', 'indian-history', 'history', 'art-and-culture', 'art-culture', 'festival', 'festivals', 'dharm', 'dharma', 'dharam', 'cultures', 'astronomy', 'india-festival', 'indian-festivals', 'religions'],
	'Science and Technology': ["auto", "automobile", "auto-mobile", "tech", "technology", "automobiles", "technology-hindi", "tech-news", "science", "tech-auto", "gadget", "gadgets", "science-environment", "environment", "technologies", "gadget-news", "science-and-future", "auto-travel", "sciences", "tech-and-auto", "auto-news", "automobile-news", "science-tech", "science-tech-news", "techonology-science", "tech-gadget", "tech-gadgets", "sci-tech", "science-and-technology", "science-technology", "technology-science"],
	'Business, Economics and Finance': ["business", "money", "business-hindi", "economy", "economies", "economic", "economics", "market", "markets", "finance", "finances", "india-business", "indian-business", "international-business", "banking-and-finance", "business-news", "economy-news", "market-news", "finance-news", "corporate", "corporate-news", "business-economy"],
	'Coronavirus': ["corona", "coronavirus", "covid", "covid-19", "covid19", "corona-virus", "coronavirus-news"],
	'Education and Career': ["education", "jobs", "career", "education-career", "career-job", "job-news", "education-news", "career-news", "education-today", "job", "career-and-courses", "education-and-job", "education-and-jobs"],
	'Health and Lifestyle': ["diet-fitness", "fitness", "nutrition", "lifestyle", "lifestyles", "tour-travel", "travel", "fashion", "beauty", "khana-khazana", "lifestyle-hindi", "travel-tour", "health", "jeevan-mantra", "jeevan", "health-fitness", "food-news", "life-style", "yoga-and-health", "pravasi", "health-news", "beauty-news", "health-and-fitness", "life-and-style", "life-and-styles"],
	'Politics': ["politics", "politics-news", "election", "elections", "politics-nation", "india-politic", "indian-politic", "india-politics", "indian-politics", "political-news", "government"],
	'Entertainment': ["moviemasala", "news-on-films", "bollywood", "bollywood-news", "filmy", "karyakrams", "karyakram", "manoranjan", "entertainment", "entertain", "entertainment-hindi", "bollywood-news", "cinema", "etime", "etimes", "movie-masti", "entertainment-news", "world-cinema"],
	'Multimedia': ["video","videos","photo","photos","photogallery","gallery","media","photo-gallery","galleries","videolist","photmazza","photoarticlelist","photo-articlelist","picture","picture-gallery","pictures","picture-gallery-section","news-video","ivideo","ivideos","multimedia"],
	'National': ["national","nation-news","nation","national-news","bharat","bhaarat","india","indian","india-news","indian-news"],
	'Privacy Policy': ["privacy", "privacy-policy", "private-policy", "privatepolicy", "privacypolicy", "privacy_policy"],
	'Sports': ["sport", "sports", "sports-news", "cricket-hindi", "cricket-news", "gaming", "games", "sport-news"],
	'Regional': ["state", "states-news", "states", "state-news", "regional", "region", "north-east", "northeast", "south"],
	'International': ["world", "world-news", "international", "international-news", "miscellaneous-world", "world-affair", "world-affairs"],
	'Local': ["my-city-my-pride", "city", "cities", "city-news", "local", "mycity", "mycity-talk", "location", "locations", "mirror-now", "mirror"]
}

print("\nTraining Word2Vec Model ...\n")
# Load pretrained model (since intermediate data is not included, the model cannot be refined with additional data)
# Follow details mentioned in our paper to download the pre-trained model from (http://vectors.nlpl.eu/repository/)
model = gensim.models.KeyedVectors.load_word2vec_format('./word2vecData/English Corpus/model.bin', binary=True)


def read_file(path, filename):
	f = open(os.path.join(path, filename), 'r', encoding='utf-8')
	text = f.read()
	f.close()
	return text


def filter_words(sentence):
	stop = list(set(stopwords.words('english')))
	stop.append("html")
	return [word.lower() for word in sentence if word not in stop]


def tokenize(text):
	tokenizer = RegexpTokenizer(r'\w+')
	return filter_words(tokenizer.tokenize(text))


def tokenize_urls(text):
	tokenizer = RegexpTokenizer(r'\w+')
	return [filter_words(tokenizer.tokenize(urlparse(url).path)) for url in text.split("\n")]


def get_combined_embedding_of_a_topic(list_l, send_presence):
	global topic_dictionary
	global topic_head_embeddings
	vi = [0] * 100
	presence_in_model = 0

	for i in list_l:
		for wi in tokenize(i):
			if wi in model:
				vi += model[wi]
				presence_in_model = 1
			else:
				for t in topic_dictionary.keys():
					if wi in topic_dictionary[t]:
						vi += topic_head_embeddings[t]
						break

	if send_presence == 1: 
		return vi, presence_in_model
	else: 
		return vi


def get_cosine_sim(embedding1, embedding2):
	cos_sim = dot(embedding1, embedding2)/(norm(embedding1)*norm(embedding2))
	return float(cos_sim)


def add_hindi_words(listt):
	global hindi_to_english_mapping
	tmp = []
	for w in listt:
		tmp.append(w)
		if w in hindi_to_english_mapping.keys():
			listt.append(hindi_to_english_mapping[w])
	return listt


def generate_topical_dictionary(df):
	global topic_dictionary
	global topic_head_embeddings
	global topic_total_embeddings

	for row in range(len(df)):
		topic, words = str(df.iloc[row]["manual_topic_label"]), str(df.iloc[row]["extracted_keywords"]).split(", ")
		if topic not in topic_dictionary.keys():
			topic_dictionary[topic] = []
		for w in words:
			if w not in topic_dictionary[topic]:
				topic_dictionary[topic].append(w)

	for topic in topic_dictionary.keys():
		topic_head_embeddings[topic] = get_combined_embedding_of_a_topic(add_hindi_words(topic.split()), 0)
		topic_total_embeddings[topic] = get_combined_embedding_of_a_topic(add_hindi_words(topic_dictionary[topic]), 0)


def google_translate_hindi_to_english():
	global topic_dictionary
	global hindi_to_english_mapping
	from googletrans import Translator
	translator = Translator()

	for topic in topic_dictionary.keys():
		for w in topic_dictionary[topic]:
			exception_flag = 0
			try:
				if w not in hindi_to_english_mapping.keys(): 
					translated_word = translator.translate(w, src='hi', dest='en').text
			except AttributeError:
				exception_flag = 1 # Do nothing exception has occurred
			finally:
				if exception_flag == 0:
					if translated_word.lower() != w.lower():
						hindi_to_english_mapping[w] = translated_word.lower()
				continue


def get_primary_topical_page(urls, topic):
	global primary_topical_page
	global topic_total_embeddings
	temp1 = {}
	temp2 = []
	
	if topic == 'Other': 
		return urls[0]

	for url in urls:
		parts = (urlparse(url).path).strip('/').split('/')
		s = get_cosine_sim(get_combined_embedding_of_a_topic(add_hindi_words(tokenize_urls(url)[0]), 0), topic_total_embeddings[topic])
		l = len(list(add_hindi_words(tokenize_urls(url)[0])))
		s = s/l
		temp2.append(s)
		temp1[str(s)] = url
		for part in parts:
			if part != '':
				if part in primary_topic_page[topic]:
					return url
	
	return temp1[str(sorted(temp2, reverse=True)[0])] # most similar url
	return urls[0]	# shortest url


def predict_single_best_url_for_each_topic(dictd):
	best_urls = {}
	for topic in dictd.keys():
		if topic == '': 
			continue
		overall_scores = []
		# urls = sorted(dictd[topic], key=len)[:3]
		# best_urls[topic] = urls[0]
		urls = sorted(dictd[topic], key=len)
		best_urls[topic] = get_primary_topical_page(urls, topic)

	return best_urls



def main():

	df_cnt = 0
	site_cnt = 0
	cnt = 0
	# To maintain which all topics are present in a given website
	topic_presence_counts = {'Art, Culture and Society': 0,'Science and Technology': 0,'Business, Economics and Finance': 0,'Coronavirus': 0,
							'Education and Career': 0,'Health and Lifestyle': 0,'Politics': 0,'Entertainment': 0,'Other': 0,'Multimedia': 0,
							'National': 0,'Privacy Policy': 0,'Sports': 0,'Regional': 0,'International': 0,'Local': 0}
	DATA_DIR = os.path.join(os.path.abspath(os.pardir))
	input_file_path = os.path.join(os.path.abspath(os.curdir),'Filtered URLs')
	train_data = pd.read_csv(os.path.join(DATA_DIR, "manual_topical_dictionary.csv"))
	# To output best match URL for each Topic
	final_data = pd.DataFrame(columns=['link_no', 'website_no', 'homepage_url', 'topical_url', 'topical_label'])
	# Generating a topical dictionary
	generate_topical_dictionary(train_data)

	master_all_urls = {}
	for file in os.listdir(input_file_path)[:]:
		prediction_all_urls = prediction_best_topic_url = {}
		
		cnt = cnt+1
		site_cnt = site_cnt+1
		print("\n\n\n", cnt, file)
		url_list = read_file(input_file_path, file).split("\n") 
		if len(url_list) < 5:
			continue

		for url in url_list:
			url_parts = (urlparse(url).path).strip('/').split('/')

			predicted_topic = ""
			flag = 0
			for part in url_parts[:3]:
				if part in ['category', 'categories', 'topic', 'topics', 'section', 'sections', 'news', 'pages', 'page', 'feature', 'features'] and len(url_parts) >= 2:
					url_parts = url_parts[1:]
					continue
				if url_parts.index(part) == 0:
					for t in topic_dictionary.keys():
						if part in topic_dictionary[t]:
							predicted_topic = t
							flag = 1
							break
						else: 
							continue

					if flag == 1: 
						break
					else:
						max_score = 0.4 # Obtained through bi-modal histogram
						max_topic = 'Other'

						for t in topic_dictionary.keys():
							if t != 'Other':
								score = get_cosine_sim(get_combined_embedding_of_a_topic(add_hindi_words(tokenize_urls(url)[0]), 0), topic_total_embeddings[t])
								if score > max_score:
									max_topic = t
									max_score = score
						predicted_topic = max_topic
			
			# print(predicted_topic, "|", url)
			if predicted_topic not in prediction_all_urls.keys():
				prediction_all_urls[predicted_topic] = []
			prediction_all_urls[predicted_topic].append(url)

		prediction_best_topic_url = predict_single_best_url_for_each_topic(prediction_all_urls)

		for topc in prediction_all_urls.keys():
			for siteurl in prediction_all_urls[topc]:
				master_all_urls[siteurl] = topc

		# '''
		for topic in prediction_best_topic_url.keys():
			print(topic, "|", prediction_best_topic_url[topic])
			homepage = str(urlparse(prediction_best_topic_url[topic]).scheme)+"://"+str(urlparse(prediction_best_topic_url[topic]).netloc)
			# Writing Data to a Dataframe
			final_data.loc[df_cnt] = [df_cnt+1, site_cnt, homepage, topic, prediction_best_topic_url[topic]]
			df_cnt += 1
		# '''

		for topic in topic_presence_counts.keys():
			if topic in prediction_all_urls.keys():
				if len(prediction_all_urls[topic]) > 0:
					topic_presence_counts[topic] += 1

	# for topic in topic_presence_counts.keys():
		# print(topic, ",", topic_presence_counts[topic])

	final_data.to_csv(os.path.join(DATA_DIR, "DiBETS Output Data" + '.csv'), index='False')
	

if __name__ == "__main__":
	main()
