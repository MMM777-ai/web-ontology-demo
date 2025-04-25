import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import json

# Load ontology data from file
try:
    with open("ontology_sample.json", "r") as f:
        ontology_data = json.load(f)
except FileNotFoundError:
    st.error("Ontology file (ontology_sample.json) not found. Please ensure it exists in the project directory.")
    ontology_data = {"concepts": [], "relations": []}
except json.decoder.JSONDecodeError as e:
    st.error(f"Invalid JSON in ontology_sample.json: {str(e)}. Please check the file for syntax errors (e.g., missing commas).")
    ontology_data = {"concepts": [], "relations": []}

# Page setup
st.set_page_config(page_title="OntoGuard-Inspired AI Demo", layout="wide")

# Inject custom CSS to force sidebar visibility on mobile
st.markdown("""
<style>
@media (max-width: 768px) {
    [data-testid="stSidebar"] {
        display: block !important;
        width: 100% !important;
        position: relative !important;
        min-width: unset !important;
        max-width: unset !important;
    }
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    [data-testid="stAppViewContainer"] {
        padding-top: 1rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.title("🔍 OntoGuard-Inspired AI Demo")
st.subheader("Governance Layer Beneath LLMs: Real-Time Compliance & Reliability")

# Sidebar: Prompt-to-Ontology Mapping
st.sidebar.markdown("### 🔍 Prompt-to-Ontology Mapping")
user_prompt = st.sidebar.text_input("Enter a user prompt:", placeholder="e.g., Is our sentiment model GDPR compliant?")

mapped_concepts = []
if user_prompt:
    if "hipaa" in user_prompt.lower():
        mapped_concepts = ["Compliance", "HIPAA", "Risk Assessment"]
    elif "gdpr" in user_prompt.lower():
        mapped_concepts = ["Compliance", "GDPR", "Policy Validation"]
    elif "trust" in user_prompt.lower():
        mapped_concepts = ["Trust Scoring", "Model Output"]

if mapped_concepts:
    st.sidebar.markdown("**Mapped Ontology Concepts:**")
    for concept in mapped_concepts:
        st.sidebar.markdown(f"- {concept}")

# Sidebar: White Paper and GitHub Links
st.sidebar.markdown("---")
st.sidebar.markdown("[📄 View Public White Paper](https://github.com/MMM777-ai/ontoguard/blob/main/assets/Ontology-Enhanced%20AI%20-%20Public%20White%20Paper.pdf)")
st.sidebar.markdown("[🌐 GitHub Repository](https://github.com/MMM777-ai/web-ontology-demo)")

# Prompt input (main column)
st.markdown("""
### 💬 Submit a Prompt
_Type a question or statement your LLM might generate. This demo simulates evaluation for reliability, compliance, and reasoning beneath models like GPT-4, Claude, or Gemini._
""")
if user_prompt:
    # Simulated dynamic reliability score (fake, IP-safe)
    keywords = ["compliant", "data", "model"]
    trust_score = min(95, 80 + sum(word in user_prompt.lower() for word in keywords) * 5 + len(user_prompt.split()) % 11)
    compliance_results = {
        "EU AI Act": "✅ Fully Compliant",
        "GDPR": "⚠️ Partial Compliance — Consent Clause Missing",
        "HIPAA": "✅ No Violation Detected"
    }
    risk_level = "Moderate Risk" if "⚠️" in compliance_results.values() else "Low Risk"

    st.markdown("---")
    st.markdown("### ✅ Governance Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Reliability Score", f"{trust_score}% Reliable")
    with col2:
        st.warning(f"Risk Level: {risk_level}")

    st.markdown("#### 🧾 Compliance Checks")
    with st.expander("View Compliance Details"):
        for law, result in compliance_results.items():
            st.markdown(f"**{law}**: {result}")
            if "⚠️" in result:
                st.markdown(f"- *Reason*: Simulated gap in policy adherence.")
            else:
                st.markdown(f"- *Reason*: Passes simulated regulatory evaluation.")

    st.markdown("---")
    st.markdown("### 🔗 Symbolic Reasoning Trace (Interactive Graph)")
    
    # Enhanced graph using JSON
    G = nx.DiGraph()
    for rel in ontology_data["relations"]:
        G.add_edge(rel["source"], rel["target"], label=rel["type"])
    G.add_edge("Prompt", "Data Input", label="processed by")
    G.add_edge("Data Input", "Sentiment Model", label="feeds")
    G.add_edge("Sentiment Model", "Compliance", label="evaluated by")
    G.add_edge("Compliance", "EU AI Act", label="checks")
    G.add_edge("EU AI Act", "✔ Compliant", label="passes")
    G.add_edge("Compliance", "HIPAA", label="checks")
    G.add_edge("HIPAA", "✔ Compliant", label="passes")

    # Cluster-based node coloring
    cluster_colors = {
        "AI Ethics": "green",
        "Model Governance": "blue",
        "Regulatory Risk": "orange",
        "Transparency & Explainability": "purple",
        "Data Protection": "red"
    }
    concept_to_cluster = {c["label"]: c["cluster"] for c in ontology_data["concepts"]}
    node_colors = [cluster_colors.get(concept_to_cluster.get(node, ""), "lightblue") for node in G.nodes()]

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'label')
    fig, ax = plt.subplots(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=12, arrows=True, edge_color='gray', ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    plt.title("Symbolic Reasoning Preview")
    st.pyplot(fig)

    # Cluster Legend
    st.markdown("### 🗺️ Cluster Legend")
    st.markdown("🟢 AI Ethics • 🔵 Model Governance • 🟠 Regulatory Risk • 🟣 Transparency & Explainability • 🔴 Data Protection")

    # Reasoning Paths
    st.markdown("### 🛤️ Reasoning Paths")
    reasoning_paths = [
        "Prompt → Compliance → GDPR → Regulatory Fine",
        "Prompt → Machine Learning → Model Bias → Fairness"
    ]
    for path in reasoning_paths:
        st.markdown(f"- **Path**: {path}")
    st.markdown("_These paths trace how prompts connect to impacts through the ontology._")

    st.markdown("""
    _This graph previews how an OntoGuard-inspired layer symbolically connects concepts to govern LLM reliability and compliance._
    """)

st.markdown("---")
st.markdown("""
#### 👤 Invented & Built by Mark Starobinsky
- 📜 Featured in Marquis Who's Who 2025
- 📩 [Contact via LinkedIn](https://www.linkedin.com/in/markstarobinsky)

_This redacted demo excludes proprietary drift detection, federated validation, and sub-second reasoning—unlock the full OntoGuard platform under NDA._
""")
if st.button("Request NDA Details"):
    st.markdown("📧 Please contact [markstarobinsky@yourdomain.com](mailto:markstarobinsky@yourdomain.com) to initiate NDA discussions.")