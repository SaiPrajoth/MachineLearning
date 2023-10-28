 # Emotion-Phrase Association

This code associates emotions with input phrases using pre-trained word vectors. It calculates the similarity between input phrases and predefined emotions, such as "happy," "sad," and "angry," and selects the closest emotion based on similarity.

## Usage

1. **Prerequisites:**

   - Ensure you have Python installed.
   - Install the spaCy library:
     ```
     pip install spacy
     ```
   - Download the spaCy medium-sized English model with pre-trained word vectors:
     ```
     python -m spacy download en_core_web_md
     ```

2. **Define Example Emotion Phrases:**

   Modify the example phrases for each emotion in the code. These phrases serve as references for emotions.

3. **Run the Code:**

   Execute the code, and provide an input phrase to determine the closest associated emotion.

4. **Output:**

   The code will return the emotion that best matches the input phrase based on word vector similarity.

## Notes

- This code provides a basic example for educational purposes.
- Real-world emotion analysis typically requires more extensive datasets and advanced models.

Feel free to customize and expand this code for your specific needs or to explore word vector-based emotion associations.
