import streamlit as st
import json
import time

# --------- Research Agent ---------
def research_amazon():
    info = {
        "industry": "Retail/E-commerce",
        "company": "Amazon",
        "focus_areas": [
            "Logistics and Supply Chain Management",
            "Customer Personalization",
            "Inventory Forecasting",
            "Last-mile Delivery Automation",
            "Customer Support Services"
        ],
        "vision": "To be Earth's most customer-centric company, where customers can find and discover anything they might want to buy online."
    }
    return info

# --------- Use Case Generator Agent ---------
def generate_use_cases(company_info):
    use_cases = [
        {
            "title": "🎯 Personalized Product Recommendations",
            "description": "Use AI to suggest products tailored to customer preferences and past behaviors.",
            "tech": ["Machine Learning", "Reinforcement Learning", "Recommendation Systems"]
        },
        {
            "title": "📦 Inventory Demand Forecasting",
            "description": "Predict stock requirements dynamically using ML models to optimize inventory costs.",
            "tech": ["Time Series Forecasting", "Deep Learning"]
        },
        {
            "title": "📝 GenAI for Product Descriptions",
            "description": "Automatically generate engaging product descriptions using Large Language Models (LLMs).",
            "tech": ["LLMs", "Text Generation"]
        },
        {
            "title": "💬 AI-Powered Customer Support Chatbots",
            "description": "Deploy LLMs to provide real-time support and query resolution for customers.",
            "tech": ["Chatbots", "Conversational AI"]
        }
    ]
    return use_cases

# --------- Resource Asset Collector Agent ---------
def find_resource_assets():
    resources = [
        {"name": "Retail Product Recommendation Dataset", "link": "https://www.kaggle.com/datasets/retail-product-recommendation"},
        {"name": "Retail Inventory Forecasting Dataset", "link": "https://www.kaggle.com/datasets/inventory-demand-forecasting"},
        {"name": "Amazon Customer Service Chatbot Datasets", "link": "https://www.kaggle.com/datasets/amazon-customer-support-chatbot-data"},
        {"name": "Product Description Generation Dataset", "link": "https://huggingface.co/datasets/product_description_generation"}
    ]
    return resources

# --------- Streamlit Frontend ---------

# Page configuration
st.set_page_config(
    page_title="Market Research & AI Use Case Generator",
    page_icon="🚀",
    layout="wide"
)

# Optional Background Image
def set_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1616161618511-b3c6cc8768e7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Sidebar Settings
st.sidebar.title("⚙️ Settings")
theme = st.sidebar.radio("Choose Theme:", ["Light", "Dark"])
bg_image = st.sidebar.checkbox("Add Cool Background? 🎨", value=True)

# Apply Background
if bg_image:
    set_bg()

# Main App
st.title("🚀 Market Research & AI Use Case Generator")
st.subheader("🔎 Company: **Amazon** | 🛒 Industry: **Retail/E-commerce**")

with st.expander("ℹ️ About This App"):
    st.write("""
    - Researches Amazon and Retail Industry 🌍
    - Generates **AI/GenAI/ML** based Use Cases 💡
    - Collects datasets & resources 📚
    - Lets you download the final proposal 📄
    """)

st.divider()

if st.button("✨ Run Full Analysis"):
    st.toast("Researching in progress...", icon="🔍")
    my_bar = st.progress(0)

    # Step 1: Research
    with st.spinner("Gathering Company Information..."):
        company_info = research_amazon()
        for i in range(20, 101, 20):
            my_bar.progress(i)
            time.sleep(0.2)

    st.success("✅ Research Complete!")
    st.json(company_info)
    st.divider()

    # Step 2: Use Case Generation
    st.header("🧠 AI/ML/GenAI Use Cases")
    with st.spinner("Generating Smart Solutions..."):
        use_cases = generate_use_cases(company_info)
        time.sleep(1)

    col1, col2 = st.columns(2)
    for idx, uc in enumerate(use_cases):
        with (col1 if idx % 2 == 0 else col2):
            st.markdown(f"### {uc['title']}")
            st.write(uc['description'])
            st.caption(f"Technologies: {', '.join(uc['tech'])}")
            st.divider()

    # Step 3: Collect Datasets
    st.header("📚 Resources & Datasets")
    with st.spinner("Fetching external assets..."):
        resources = find_resource_assets()
        time.sleep(1)

    for res in resources:
        st.markdown(f"- [{res['name']}]({res['link']})")

    # Step 4: Create Final Markdown
    final_md = "# Final Proposal for Amazon (Retail)\n\n"
    final_md += "## Company Research\n"
    final_md += json.dumps(company_info, indent=2)
    final_md += "\n\n## Use Cases\n"
    for uc in use_cases:
        final_md += f"### {uc['title']}\n"
        final_md += f"{uc['description']}\n"
        final_md += f"**Technologies**: {', '.join(uc['tech'])}\n\n"
    final_md += "## Resource Assets\n"
    for res in resources:
        final_md += f"- [{res['name']}]({res['link']})\n"

    # Final Download
    # After the "Final Report" is generated:

st.balloons()
st.success("🎉 Analysis Complete! Download Options Below:")

# Download Markdown
st.download_button(
    label="📥 Download Proposal (Markdown)",
    data=final_md,
    file_name="final_proposal.md",
    mime="text/markdown"
)

# Download PDF
pdf_file = generate_pdf(company_info, use_cases, resources)
st.download_button(
    label="📄 Download Proposal (PDF)",
    data=pdf_file,
    file_name="final_proposal.pdf",
    mime="application/pdf"
)
