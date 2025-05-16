import numpy as np
import json
import spacy
import streamlit as st

# Load resumes and job opportunities from JSON files
with open('resumes.json', 'r') as f:
    resumes = json.load(f)

with open('job_opportunities.json', 'r') as f:
    jobs = json.load(f)

# Load the large English model from spaCy
nlp = spacy.load('en_core_web_lg')

# Function to compute an embedding vector from a list of keywords
def get_embedding_from_keywords(keywords):
    # Join keywords into one text string and process with spaCy
    doc = nlp(" ".join(keywords))
    return doc.vector

# Precompute embeddings for all resumes and jobs
resume_embeddings = [
    get_embedding_from_keywords(resume["key_words"])
    for resume in resumes
]
job_embeddings = [
    get_embedding_from_keywords(job["key_words"])
    for job in jobs
]

# Print embedding shapes for debugging
print(f'resume_embeddings shape is: {np.array(resume_embeddings).shape}')
print(f'job_embeddings shape is : {np.array(job_embeddings).shape}')

# Euclidean distance helper function
def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

# Find the top N resumes closest to a given job embedding
def match_resumes_to_job(job_embedding, resume_embeddings, top_n=3):
    distances = [
        euclidean_distance(job_embedding, resume_embedding)
        for resume_embedding in resume_embeddings
    ]
    # Get indices of the smallest distances
    top_indices = np.argsort(distances)[:top_n]
    return top_indices, [distances[i] for i in top_indices]

# Optional: test matching logic in the console
if __name__ == "__main__":
    job = jobs[0]
    job_embedding = job_embeddings[0]
    indices, scores = match_resumes_to_job(job_embedding, resume_embeddings)
    print(f"\n🔍 Top {len(indices)} Matching Resumes for Job: {job['title']}\n")
    for rank, idx in enumerate(indices, start=1):
        print(f"#{rank} - Resume Title: {resumes[idx]['title']} | Distance: {scores[rank-1]:.4f}")

# --- Streamlit App UI ---
st.title("🧠 Resume-to-Job Matching App")

# Dropdown to select a job opening
selected_job_title = st.selectbox(
    "Select a Job Opening",
    [job["title"] for job in jobs]
)

# Find the index of the selected job
selected_index = next(
    (i for i, job in enumerate(jobs) if job["title"] == selected_job_title),
    None
)

if selected_index is not None:
    selected_job = jobs[selected_index]
    selected_embedding = job_embeddings[selected_index]

    # Display job title
    st.header(f"💼 Job: {selected_job['title']}")
    # Display job description
    st.markdown(f"**Description:** {selected_job['text']}")
    # Display job keywords
    st.markdown("**Keywords:**")
    st.write(", ".join(selected_job["key_words"]))

    st.markdown("---")

    # Compute top 3 matching resumes
    indices, scores = match_resumes_to_job(
        selected_embedding,
        resume_embeddings,
        top_n=3
    )

    st.subheader("🔍 Top 3 Matching Resumes")
    for rank, idx in enumerate(indices, start=1):
        resume = resumes[idx]
        # Display resume title
        st.markdown(f"### #{rank}: {resume['title']}")
        # Display resume ID
        st.markdown(f"- **ID:** `{resume['id']}`")
        # Display similarity score
        st.markdown(f"- **Similarity Score (lower is better):** {scores[rank-1]:.4f}")
        # Display resume summary
        st.markdown(f"- **Summary:** {resume['text']}")
        # Display resume keywords
        st.markdown(f"- **Keywords:** {', '.join(resume['key_words'])}")
        st.markdown("---")

# streamlit run matcher_app.py