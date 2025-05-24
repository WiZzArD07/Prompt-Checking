"""
Streamlit web interface for the AI Jailbreaking Prompt Checker
"""

import streamlit as st
import pandas as pd
from prompt_checker import PromptChecker
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="AI Jailbreaking Prompt Checker",
    page_icon="🛡️",
    layout="wide"
)

# Initialize the prompt checker
checker = PromptChecker()

# Title and description
st.title("🛡️ AI Jailbreaking Prompt Checker")
st.markdown("""
This tool helps detect potential jailbreaking attempts in prompts sent to AI models.
Enter your prompt below to analyze it for potential security risks.
""")

# Create two columns for input and results
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Input Prompt")
    prompt = st.text_area(
        "Enter your prompt here:",
        height=200,
        placeholder="Type or paste your prompt here..."
    )
    
    analyze_button = st.button("Analyze Prompt", type="primary")

with col2:
    st.subheader("Analysis Results")
    
    if analyze_button and prompt:
        # Analyze the prompt
        result = checker.analyze_prompt(prompt)
        
        # Display risk score with color-coded gauge
        risk_score = result["risk_score"]
        risk_color = "green" if risk_score < 0.3 else "orange" if risk_score < 0.7 else "red"
        
        st.markdown(f"""
        <div style='text-align: center'>
            <h3>Risk Score: <span style='color: {risk_color}'>{risk_score:.2f}</span></h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Create gauge chart
        fig = px.pie(
            values=[risk_score, 1-risk_score],
            names=["Risk", "Safe"],
            hole=0.7,
            color_discrete_sequence=[risk_color, "lightgray"]
        )
        fig.update_layout(
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0),
            height=200
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Display safety status
        safety_status = "✅ Safe" if result["is_safe"] else "⚠️ Potentially Unsafe"
        st.markdown(f"### Status: {safety_status}")
        
        # Display warnings if any
        if result["warnings"]:
            st.markdown("### ⚠️ Warnings")
            for warning in result["warnings"]:
                st.markdown(f"- {warning}")
        
        # Display detected patterns
        if result["detected_patterns"]:
            st.markdown("### 🔍 Detected Patterns")
            patterns_df = pd.DataFrame(result["detected_patterns"])
            st.dataframe(
                patterns_df,
                column_config={
                    "description": "Pattern Description",
                    "weight": st.column_config.NumberColumn(
                        "Risk Weight",
                        format="%.2f"
                    )
                },
                hide_index=True
            )
    elif analyze_button:
        st.warning("Please enter a prompt to analyze.")

# Add footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with ❤️ using Streamlit and Python</p>
</div>
""", unsafe_allow_html=True) 