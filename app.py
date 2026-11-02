
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 FAQ Chatbot")
st.write("Ask a question and get an answer instantly.")

# Frequently asked questions and answers
faq_data = {
    "What is artificial intelligence?":
        "Artificial Intelligence (AI) is a field of computer science that enables machines to perform tasks that normally require human intelligence.",

    "What is machine learning?":
        "Machine Learning is a branch of AI that allows computers to learn patterns from data and make predictions.",

    "What is deep learning?":
        "Deep Learning is a type of machine learning that uses neural networks with multiple layers to learn complex patterns.",

    "What is Python?":
        "Python is a popular, high-level programming language used in web development, data science, automation, and artificial intelligence.",

    "What is a chatbot?":
        "A chatbot is a software application that communicates with users through text or voice and provides automated responses.",

    "What is data science?":
        "Data Science is the field of collecting, analyzing, and interpreting data to discover useful information and support decisions.",

    "What is natural language processing?":
        "Natural Language Processing (NLP) is a branch of AI that helps computers understand, interpret, and process human language.",

    "What is a neural network?":
        "A neural network is a machine learning model inspired by the human brain. It consists of connected processing units called neurons.",

    "What is supervised learning?":
        "Supervised learning is a machine learning approach where a model learns from labeled training data.",

    "What is unsupervised learning?":
        "Unsupervised learning is a machine learning approach where a model finds patterns in data without labeled answers."
}

questions = list(faq_data.keys())
answers = list(faq_data.values())

# Convert FAQ questions into numerical vectors
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

# User input
user_question = st.text_input(
    "Enter your question:",
    placeholder="For example: What is machine learning?"
)

# Similarity threshold
similarity_threshold = 0.25

if st.button("Get Answer", use_container_width=True):

    if not user_question.strip():
        st.warning("Please enter a question.")

    else:
        # Convert user question into a vector
        user_vector = vectorizer.transform([user_question])

        # Calculate similarity scores
        similarity_scores = cosine_similarity(
            user_vector,
            faq_vectors
        )[0]

        best_match_index = similarity_scores.argmax()
        best_score = similarity_scores[best_match_index]

        # Display the best matching answer
        if best_score >= similarity_threshold:
            st.success("Answer found!")
            st.subheader("Chatbot Answer")
            st.write(answers[best_match_index])
            st.caption(f"Matching confidence: {best_score:.2f}")

        else:
            st.warning(
                "Sorry, I couldn't find a suitable answer. "
                "Please try asking another question."
            )

st.divider()
st.caption("FAQ Chatbot | CodeAlpha Artificial Intelligence Internship")
