import streamlit as st
from groq import Groq

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Content Studio",
    page_icon="✍️",
    layout="centered"
)

# ----------------------------
# Groq Client
# ----------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ----------------------------
# Title
# ----------------------------
st.title("✍️ AI Content Studio")
st.caption("Create high-quality AI-generated content in seconds.")

st.markdown("---")

# ----------------------------
# Input Form
# ----------------------------
with st.container():

    col1, col2 = st.columns(2)

    with col1:
        content_type = st.selectbox(
            "Content Type",
            [
                "Blog Post",
                "LinkedIn Post",
                "Professional Email",
                "Instagram Caption",
                "Advertisement",
                "YouTube Script"
            ]
        )

    with col2:
        tone = st.selectbox(
            "Tone",
            [
                "Professional",
                "Friendly",
                "Formal",
                "Creative",
                "Persuasive"
            ]
        )

    topic = st.text_input(
        "Topic",
        placeholder="Example: Artificial Intelligence in Healthcare"
    )

    length = st.selectbox(
        "Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )

    additional = st.text_area(
        "Additional Instructions (Optional)",
        placeholder="Mention anything specific you want the AI to include..."
    )

st.markdown("")

generate = st.button(
    "🚀 Generate Content",
    use_container_width=True
)

# ----------------------------
# Generate Content
# ----------------------------
if generate:

    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic.")
        st.stop()

    if content_type == "Blog Post":
        instruction = "Write a detailed blog post with an engaging introduction, headings, and conclusion."

    elif content_type == "LinkedIn Post":
        instruction = "Write a professional LinkedIn post. End with relevant hashtags."

    elif content_type == "Professional Email":
        instruction = "Write a professional email including a subject line, greeting, body, and closing."

    elif content_type == "Instagram Caption":
        instruction = "Write an engaging Instagram caption with emojis and hashtags."

    elif content_type == "Advertisement":
        instruction = "Write persuasive advertising copy with a catchy headline and a strong call-to-action."

    else:
        instruction = "Write a YouTube video script with an introduction, main content, and conclusion."

    prompt = f"""
You are an expert content writer.

{instruction}

Topic:
{topic}

Tone:
{tone}

Length:
{length}

Additional Instructions:
{additional}

Ensure the content is well-structured, engaging, and easy to read.
"""

    with st.spinner("Generating content..."):

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert AI content writer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1200
        )

    result = response.choices[0].message.content

    st.success("✅ Content generated successfully!")

    st.markdown("---")

    with st.expander("📄 View Generated Content", expanded=True):
        st.markdown(result)

    word_count = len(result.split())

    st.info(f"📝 Word Count: **{word_count}**")

    st.caption(
        f"Content Type: **{content_type}** | Tone: **{tone}** | Length: **{length}**"
    )

    st.download_button(
        label="📥 Download as TXT",
        data=result,
        file_name="generated_content.txt",
        mime="text/plain",
        use_container_width=True
    )

# ----------------------------
# About Section
# ----------------------------

st.markdown("---")

st.subheader("ℹ️ About this App")

st.write("""
AI Content Studio is an AI-powered content generation application that helps users create blogs, LinkedIn posts, professional emails, Instagram captions, advertisements, and YouTube scripts using Groq's Llama 3.3 70B model.

Users can customize the content type, tone, length, and additional instructions to generate high-quality content tailored to their needs.
""")

# ----------------------------
# Footer
# ----------------------------

st.markdown("---")

st.caption(
    "Developed by Archit Ravikumar • Powered by Groq (Llama 3.3 70B) • Built with Streamlit"
)