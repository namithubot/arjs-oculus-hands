
def get_encodings(message_file):
	'''
		Reads message_file and provide a map
		constaing digits and their mapped strings.
	'''
	# Read the file lines
	file = open(message_file, 'r')
	Lines = file.readlines()
	
	# Initialize empty encodings
	encodings = {}

	# Get the encodings from each line
	for line in Lines:
		encoding_pair = line.split(' ')
		# Make sure that the value doesn't have newline character
		encodings[int(encoding_pair[0])] = encoding_pair[1].strip()
	
	return encodings

def get_pyramid_encoded_sentence(max):
	'''
		Based on given max values, returns an array
		which denotes the last number in each step of pyramid
	'''
	# Start with the top sentence
	sentence = [1]
	last_word = 1
	step = 1
	while last_word < max:
		step = step + 1
		last_word = last_word + step
		sentence.append(last_word)
	return sentence

def get_decoded_sentence(encodings, encoded_sentence):
	'''
		Decodes a sentence based on the encodings provided
	'''
	sentence_array = []
	for encoded_word in encoded_sentence:
		sentence_array.append(encodings[encoded_word].lower())
	return sentence_array

def decode(message_file):
	'''
		Decodes a pyramid based on the encodings
		provided in message_file
	'''
	encodings = get_encodings(message_file)
	encoded_sentence = get_pyramid_encoded_sentence(max(encodings.keys()))
	return " ".join(get_decoded_sentence(encodings, encoded_sentence))

print(decode('coding_qual_input.txt'))

	