![004810@2x](https://github.com/Soft-Bred/Customer-Feedback-Analysis-Program/assets/60551230/3759c7e1-7f5a-482c-83ad-4eef01b354f6)


# **Customer Feedback Analysis Program**

The main goal of the customer feedback analysis tool is to help businesses improve their services by looking at what customers have to say. Businesses that get a lot of customer feedback and want to find common themes and feelings so they can make changes will find the app useful. Customer service reps, marketing teams, and product development teams are usually the ones who use this app.

---

## **Installation**

1. Install [*these dependencies*](https://github.com/Soft-Bred/Customer-Feedback-Analysis-Program/tree/main#dependencies) by running the following command

```bash
pip install PyQt6 nltk scikit-learn && python -m nltk.downloader punkt wordnet stopwords vader_lexicon
```

1. Open the `Customer Feedback Analysis Program.py` file into your preferred IDE.
2. Run the script.

---
## **Demonstration**

[YouTube Video](https://youtu.be/D5xNHWSoYXE)

---

## Dependencies

### PyQt6

PyQt6 is used to build the application's entire graphical user interface (GUI). This means making the main window, setting its size, and putting all the widgets (like buttons and labels) in the right place.

### NLTK (Natural Language Toolkit)

NLTK is primarily used for the purpose of text preprocessing and sentiment analysis. Specifically, it's used to:
- Tokenize the text, which is the process of splitting the text into individual words.
- Lemmatize the words, which means converting a word to its base form (e.g., "running" would be converted to "run").
- Remove English stop words from the text, which are commonly occurring words like "the", "is", etc., that don't provide significant meaning in the context of text analysis.
- Calculate sentiment scores for the processed text.

### scikit-learn

Scikit-learn is used in the script to do something called "feature extraction," which is part of analysing text. It is used in particular to use the TfidfVectorizer to turn the processed text into a matrix of TF-IDF features. Term Frequency-Inverse Document Frequency (TF-IDF) is a number that shows how important a word is to a document in a collection or corpus.
