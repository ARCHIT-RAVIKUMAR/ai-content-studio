# ✍️ AI Content Studio

## Participant Details

- **Name:** Archit Ravikumar
- **MUID:** architravikumar@mulearn

---

## Project Overview

AI Content Studio is an AI-powered content generation web application that helps users quickly create high-quality written content. The application allows users to generate blogs, LinkedIn posts, professional emails, Instagram captions, advertisements, and YouTube scripts by leveraging a Large Language Model.

The application provides an intuitive interface where users can choose the content type, writing tone, content length, and additional instructions to generate customized results.

---

## Chosen Use Case

Content creation is a common task for students, professionals, marketers, and creators. AI Content Studio simplifies this process by generating well-structured and engaging content within seconds.

---

## AI Platform / Model Used

- **Platform:** Groq API
- **Model:** Llama 3.3 70B Versatile

---

## Features

- Generate multiple types of content
- Customizable tone
- Adjustable content length
- Additional instruction support
- Prompt engineering for different content types
- Download generated content as a text file
- Clean Streamlit interface

---

## Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile

---

## Installation

Clone the repository:

```bash
git clone <repository-link>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create:

```
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY="YOUR_API_KEY"
```

Run:

```bash
streamlit run app.py
```

---

## Key Observations

- Prompt engineering significantly improves response quality.
- Different tones produce noticeably different writing styles.
- Groq API provides very fast responses suitable for real-time applications.
- Streamlit enables rapid development of interactive AI applications.

---

## Challenges Faced

- Gemini API quota limitations required switching to Groq.
- Designing prompts that consistently generated high-quality content.
- Organizing the user interface for better usability.

---

## Future Improvements

- Export content as PDF and DOCX
- Save generation history
- Support multiple languages
- Add additional AI models
- Enable user authentication

---

## Deployment

[Live App](https://ai-content-studio-12.streamlit.app/)

---
