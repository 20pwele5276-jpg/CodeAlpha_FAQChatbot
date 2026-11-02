# FAQ Chatbot

## About
This project is an AI-based FAQ chatbot developed using Python and Streamlit. It answers frequently asked questions by finding the most similar question from a predefined FAQ dataset.

## Features
- Interactive chatbot interface
- TF-IDF text vectorization
- Cosine similarity for question matching
- Automatic answer retrieval
- Similarity threshold for handling unknown questions
- Matching confidence score

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- TF-IDF
- Cosine Similarity

## Installation

1. Clone the repository:
   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the chatbot:
   ```bash
   streamlit run app.py
   ```

## How It Works
The chatbot converts stored FAQ questions into numerical vectors using TF-IDF. When a user enters a question, cosine similarity measures how closely it matches the stored questions. The chatbot returns the answer associated with the closest match if the similarity score meets the required threshold.

## Internship
Developed as part of the CodeAlpha Artificial Intelligence Internship.

## Author
Wajiha Gul