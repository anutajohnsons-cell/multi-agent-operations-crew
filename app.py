import streamlit as st
from main import graph

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Multi-Agent Operations Crew",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0b1120, #111c32);
    color: #f1f5f9;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

.hero {
    padding: 35px;
    border-radius: 18px;
    background: linear-gradient(120deg, #172554, #312e81);
    border: 1px solid #3730a3;
    margin-bottom: 30px;
}

.hero h1 {
    color: #ffffff;
    font-size: 38px;
    margin-bottom: 10px;
}

.hero p {
    color: #cbd5e1;
    font-size: 16px;
}

.section-title {
    color: #e2e8f0;
    font-size: 23px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

.agent-card {
    background: #17243b;
    border: 1px solid #334155;
    padding: 16px 8px;
    border-radius: 12px;
    text-align: center;
    color: #e2e8f0;
    font-size: 14px;
    min-height: 85px;
}

div.stButton > button,
div.stFormSubmitButton > button {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-weight: 600;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    background: #6366f1;
    color: white;
    border: none;
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    background-color: #17243b;
    color: white;
    border: 1px solid #475569;
    border-radius: 10px;
}

div[data-testid="stTabs"] button {
    color: #cbd5e1;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <h1>🤖 Multi-Agent Operations Crew</h1>
    <p>
        An intelligent multi-agent AI system powered by LangGraph.
        Specialized AI agents collaborate to research, analyze,
        write and review your requests.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- AGENT WORKFLOW ----------------

st.markdown(
    '<div class="section-title">⚙️ Meet Your AI Team</div>',
    unsafe_allow_html=True
)

agents = [
    ("🎯", "Supervisor"),
    ("🔎", "Researcher"),
    ("📊", "Analyst"),
    ("📝", "Writer"),
    ("🔍", "Reviewer")
]

columns = st.columns(5)

for column, agent in zip(columns, agents):
    with column:
        st.markdown(
            f"""
            <div class="agent-card">
                <div style="font-size:25px">{agent[0]}</div>
                <b>{agent[1]}</b>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------- USER INPUT ----------------

st.markdown(
    '<div class="section-title">💬 Enter Your Request</div>',
    unsafe_allow_html=True
)

with st.form("request_form"):

    user_request = st.text_input(
        "What would you like the AI team to analyze?",
        placeholder="Example: Artificial Intelligence in healthcare"
    )

    submitted = st.form_submit_button(
        "🚀 Run AI Team",
        use_container_width=True
    )


# ---------------- PROCESS REQUEST ----------------

if submitted:

    if not user_request.strip():
        st.warning("Please enter a topic first.")

    else:
        try:

            with st.spinner(
                "🤖 Your AI team is working together..."
            ):

                result = graph.invoke({
                    "user_request": user_request.strip(),
                    "next_agent": "",
                    "research": "",
                    "analysis": "",
                    "final_report": "",
                    "review": "",
                    "revised_report": ""
                })

            st.success("✅ Your AI team completed the task!")

            # ---------------- RESULTS ----------------

            st.markdown(
                '<div class="section-title">📋 AI Team Results</div>',
                unsafe_allow_html=True
            )

            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "🔎 Research",
                "📊 Analysis",
                "📝 Final Report",
                "🔍 Review",
                "✨ Improved Report"
            ])

            with tab1:
                st.markdown("### Research Findings")
                st.write(
                    result.get("research", "No research available.")
                )

            with tab2:
                st.markdown("### Analysis")
                st.write(
                    result.get("analysis", "No analysis available.")
                )

            with tab3:
                st.markdown("### Final Report")
                st.write(
                    result.get("final_report", "No final report available.")
                )

            with tab4:
                st.markdown("### Reviewer Feedback")
                st.write(
                    result.get("review", "No review available.")
                )

            with tab5:
                st.markdown("### Improved Final Report")
                st.write(
                    result.get("revised_report", "No revised report available.")
                )

        except Exception as error:
            st.error(f"Unable to complete the task: {error}")


# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#94a3b8; padding:15px;">
        Multi-Agent Operations Crew<br>
        Built with Python • LangGraph • Ollama • Llama 3.2 • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)