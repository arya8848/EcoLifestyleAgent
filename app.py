import streamlit as st
from rag import retrieve_context
from granite import ask_granite

st.set_page_config(
    page_title="Eco Lifestyle Agent",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Eco Lifestyle Agent")
st.caption("Powered by IBM Granite + Retrieval-Augmented Generation (RAG)")

st.markdown("""
Ask questions about:
- ♻️ Recycling
- 🌍 Sustainable Living
- ⚡ Energy Conservation
- 💧 Water Saving
- 🌞 Renewable Energy
- 🗑️ Waste Management
""")

question = st.text_input(
    "Ask your question:",
    placeholder="Example: How can I reduce plastic use at home?"
)


if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Searching documents..."):

            context = retrieve_context(question)

        with st.spinner("Generating answer using IBM Granite..."):

            answer = ask_granite(question, context)

        st.success("Answer Generated!")

        st.markdown("## 🤖 Answer")

        st.info(answer)

        with st.expander("📄 Retrieved Context"):

            st.write(context)
        with st.sidebar:

            st.header("🌿 About")

            st.write("""
        This AI assistant helps users adopt a greener lifestyle.

        It uses:

        • IBM Granite
        • RAG
        • FAISS
        • Official Government Documents
        """)

            st.divider()

        st.markdown("### 💡 Example Questions")

        examples = [
            "How should plastic waste be managed?",
            "How can I save electricity?",
            "What is e-waste?",
            "What are the benefits of solar energy?",
        ]

        for q in examples:
            st.write("•", q)

        if st.sidebar.button("🗑 Clear Chat"):
            st.session_state.history = []
            st.rerun()

        st.divider()

        st.markdown(
        """
        <center>

        🌱 Eco Lifestyle Agent

        Built using IBM Granite, RAG, FAISS and Streamlit
        
        </center>
        """,
        unsafe_allow_html=True
        )