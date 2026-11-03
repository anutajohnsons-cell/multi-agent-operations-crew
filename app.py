import streamlit as st
from main import graph

st.set_page_config(
    page_title="Multi-Agent Operations Crew",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent Operations Crew")

st.write(
    "A LangGraph-powered multi-agent AI system "
    "that uses specialized agents to process user requests."
)

st.divider()

st.subheader("💬 Enter Your Request")

user_request = st.text_input(
    "What would you like the AI team to analyze?",
    placeholder="Example: Artificial Intelligence in healthcare"
)

if st.button("🚀 Run AI Team", use_container_width=True):

    if not user_request.strip():
        st.warning("⚠️ Please enter a topic first.")

    else:
        try:
            with st.spinner("🤖 AI team is working..."):

                result = graph.invoke({
                    "user_request": user_request.strip(),
                    "next_agent": "",
                    "research": "",
                    "analysis": "",
                    "final_report": "",
                    "review": "",
                    "revised_report": ""
                })

            st.success("✅ AI team completed the task!")

            st.subheader("🔎 Research")
            with st.container(border=True):
                st.write(
                    result.get("research", "No research available.")
                )

            st.subheader("📊 Analysis")
            with st.container(border=True):
                st.write(
                    result.get("analysis", "No analysis available.")
                )

            st.subheader("📝 Final Report")
            with st.container(border=True):
                st.write(
                    result.get("final_report", "No final report available.")
                )
            st.subheader("✨ Improved Final Report")
            with st.container(border=True):
              st.write(
                    result.get("revised_report", "No revised report available.")
                 )
            st.subheader("🔍 Reviewer Feedback")
            with st.container(border=True):
                st.write(
                    result.get("review", "No review available.")
                )

        except Exception as error:
            st.error(f"Unable to complete the task: {error}")

st.divider()

st.caption(
    "Built with Python • LangGraph • Ollama • Llama 3.2 • Streamlit"
)