import spacy

# Load the pre-trained word vectors model
word_vectors_model = spacy.load("en_core_web_md")

# Define example phrases for each emotion
happy_emotion_phrases = ["joyful", "content", "celebrating"]
sad_emotion_phrases = ["gloomy", "unhappy", "depressed"]
angry_emotion_phrases = ["furious", "enraged", "irritated"]

# Create lists of word vectors for emotion phrases
happy_emotion_vectors = [word_vectors_model(phrase).vector for phrase in happy_emotion_phrases]
sad_emotion_vectors = [word_vectors_model(phrase).vector for phrase in sad_emotion_phrases]
angry_emotion_vectors = [word_vectors_model(phrase).vector for phrase in angry_emotion_phrases]

# Calculate the average vectors for each emotion
average_happy_emotion_vector = sum(happy_emotion_vectors) / len(happy_emotion_vectors)
average_sad_emotion_vector = sum(sad_emotion_vectors) / len(sad_emotion_vectors)
average_angry_emotion_vector = sum(angry_emotion_vectors) / len(angry_emotion_vectors)

def associate_emotion_with_phrase(input_phrase):
    input_phrase_vector = word_vectors_model(input_phrase).vector

    # Calculate similarities between the input phrase vector and emotion average vectors
    similarity_to_happy = input_phrase_vector.dot(average_happy_emotion_vector)
    similarity_to_sad = input_phrase_vector.dot(average_sad_emotion_vector)
    similarity_to_angry = input_phrase_vector.dot(average_angry_emotion_vector)

    # Create a dictionary of emotion similarities
    emotion_similarities = {
        "happy": similarity_to_happy,
        "sad": similarity_to_sad,
        "angry": similarity_to_angry
    }

    # Find the emotion with the highest similarity
    closest_emotion = max(emotion_similarities, key=emotion_similarities.get)

    return closest_emotion


# Test the emotion association
input_phrase = "feeling joyous and content"
closest_emotion = associate_emotion_with_phrase(input_phrase)
print(f"The emotion associated with '{input_phrase}' is: {closest_emotion}")
