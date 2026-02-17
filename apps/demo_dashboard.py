"""
IMGO v1.0.0-alpha - Streamlit Demo Dashboard
Intelligent Multi-Framework Integrated Ontology-based GraphRAG

This is a simplified demonstration version with sample data (N=10).
Full ISGO v2.1 features available through research collaboration.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="IMGO Demo",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Constants
DATA_PATH = Path("data/sample")
VERSION = "1.0.0-alpha"

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffc107;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load all sample datasets"""
    try:
        nist_controls = pd.read_csv(DATA_PATH / "sample_nist_controls.csv")
        mitre_techniques = pd.read_csv(DATA_PATH / "sample_mitre_techniques.csv")
        ai_rmf_mapping = pd.read_csv(DATA_PATH / "sample_ai_rmf_mapping.csv")
        nist_mitre_mapping = pd.read_csv(DATA_PATH / "sample_nist_mitre_mapping.csv")
        
        with open(DATA_PATH / "sample_graphrag_paths.json", 'r') as f:
            graphrag_paths = json.load(f)
        
        return {
            'nist_controls': nist_controls,
            'mitre_techniques': mitre_techniques,
            'ai_rmf_mapping': ai_rmf_mapping,
            'nist_mitre_mapping': nist_mitre_mapping,
            'graphrag_paths': graphrag_paths
        }
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def main():
    """Main application"""
    
    # Header
    st.markdown('<div class="main-header">🔒 IMGO Demo</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-header">Intelligent Multi-Framework Integrated Ontology-based GraphRAG</div>',
        unsafe_allow_html=True
    )
    
    # Warning box
    st.markdown("""
    <div class="warning-box">
        ⚠️ <strong>Demo Version</strong>: This dashboard displays sample data (N=10) for demonstration purposes only.
        Full ISGO v2.1 system with complete datasets and GraphRAG capabilities is available through research collaboration.
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    data = load_data()
    if data is None:
        st.error("Failed to load data. Please check data files.")
        return
    
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select View",
        ["Overview", "NIST Controls", "MITRE Techniques", "AI RMF Mapping", 
         "NIST-MITRE Relationships", "Knowledge Paths", "About"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info(f"**Version**: {VERSION}\n\n**Sample Size**: N=10 per dataset")
    
    # Page routing
    if page == "Overview":
        show_overview(data)
    elif page == "NIST Controls":
        show_nist_controls(data['nist_controls'])
    elif page == "MITRE Techniques":
        show_mitre_techniques(data['mitre_techniques'])
    elif page == "AI RMF Mapping":
        show_ai_rmf_mapping(data['ai_rmf_mapping'])
    elif page == "NIST-MITRE Relationships":
        show_nist_mitre_relationships(data['nist_mitre_mapping'])
    elif page == "Knowledge Paths":
        show_knowledge_paths(data['graphrag_paths'])
    elif page == "About":
        show_about()

def show_overview(data):
    """Overview dashboard"""
    st.header("📊 Overview Dashboard")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("NIST Controls", len(data['nist_controls']))
    with col2:
        st.metric("MITRE Techniques", len(data['mitre_techniques']))
    with col3:
        st.metric("AI RMF Mappings", len(data['ai_rmf_mapping']))
    with col4:
        st.metric("Knowledge Paths", len(data['graphrag_paths']['knowledge_paths']))
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("NIST Control Priorities")
        priority_counts = data['nist_controls']['priority'].value_counts()
        fig = px.pie(
            values=priority_counts.values,
            names=priority_counts.index,
            title="Distribution by Priority",
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("MITRE Attack Tactics")
        tactic_counts = data['mitre_techniques']['tactic'].value_counts()
        fig = px.bar(
            x=tactic_counts.index,
            y=tactic_counts.values,
            labels={'x': 'Tactic', 'y': 'Count'},
            title="Techniques by Tactic",
            color=tactic_counts.values,
            color_continuous_scale='Reds'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Relationship summary
    st.subheader("NIST-MITRE Relationship Types")
    mapping_types = data['nist_mitre_mapping']['mapping_type'].value_counts()
    fig = px.bar(
        x=mapping_types.index,
        y=mapping_types.values,
        labels={'x': 'Relationship Type', 'y': 'Count'},
        title="Distribution of Mapping Types",
        color=mapping_types.values,
        color_continuous_scale='Greens'
    )
    st.plotly_chart(fig, use_container_width=True)

def show_nist_controls(df):
    """NIST Controls view"""
    st.header("🛡️ NIST SP 800-53 Controls")
    
    st.info("Displaying sample of NIST SP 800-53 Rev. 5 security controls (N=10)")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        families = ['All'] + sorted(df['family'].unique().tolist())
        selected_family = st.selectbox("Filter by Family", families)
    with col2:
        priorities = ['All'] + sorted(df['priority'].unique().tolist())
        selected_priority = st.selectbox("Filter by Priority", priorities)
    
    # Apply filters
    filtered_df = df.copy()
    if selected_family != 'All':
        filtered_df = filtered_df[filtered_df['family'] == selected_family]
    if selected_priority != 'All':
        filtered_df = filtered_df[filtered_df['priority'] == selected_priority]
    
    # Display
    st.dataframe(filtered_df, use_container_width=True, height=400)
    
    st.markdown(f"**Showing {len(filtered_df)} of {len(df)} controls**")

def show_mitre_techniques(df):
    """MITRE Techniques view"""
    st.header("⚔️ MITRE ATT&CK Techniques")
    
    st.info("Displaying sample of MITRE ATT&CK techniques (N=10)")
    
    # Filters
    tactics = ['All'] + sorted(df['tactic'].unique().tolist())
    selected_tactic = st.selectbox("Filter by Tactic", tactics)
    
    # Apply filter
    filtered_df = df.copy()
    if selected_tactic != 'All':
        filtered_df = filtered_df[filtered_df['tactic'] == selected_tactic]
    
    # Display
    st.dataframe(filtered_df, use_container_width=True, height=400)
    
    st.markdown(f"**Showing {len(filtered_df)} of {len(df)} techniques**")

def show_ai_rmf_mapping(df):
    """AI RMF Mapping view"""
    st.header("🤖 NIST AI RMF to NIST 800-53 Mappings")
    
    st.info("Displaying AI Risk Management Framework mappings to security controls (N=10)")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        functions = ['All'] + sorted(df['ai_rmf_function'].unique().tolist())
        selected_function = st.selectbox("Filter by AI RMF Function", functions)
    with col2:
        risk_levels = ['All'] + sorted(df['risk_level'].unique().tolist())
        selected_risk = st.selectbox("Filter by Risk Level", risk_levels)
    
    # Apply filters
    filtered_df = df.copy()
    if selected_function != 'All':
        filtered_df = filtered_df[filtered_df['ai_rmf_function'] == selected_function]
    if selected_risk != 'All':
        filtered_df = filtered_df[filtered_df['risk_level'] == selected_risk]
    
    # Display
    st.dataframe(filtered_df, use_container_width=True, height=400)
    
    st.markdown(f"**Showing {len(filtered_df)} of {len(df)} mappings**")

def show_nist_mitre_relationships(df):
    """NIST-MITRE Relationships view"""
    st.header("🔗 NIST-MITRE Relationship Mappings")
    
    st.info("Displaying relationships between NIST controls and MITRE techniques (N=10)")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        mapping_types = ['All'] + sorted(df['mapping_type'].unique().tolist())
        selected_type = st.selectbox("Filter by Mapping Type", mapping_types)
    with col2:
        confidences = ['All'] + sorted(df['confidence'].unique().tolist())
        selected_confidence = st.selectbox("Filter by Confidence", confidences)
    
    # Apply filters
    filtered_df = df.copy()
    if selected_type != 'All':
        filtered_df = filtered_df[filtered_df['mapping_type'] == selected_type]
    if selected_confidence != 'All':
        filtered_df = filtered_df[filtered_df['confidence'] == selected_confidence]
    
    # Display
    st.dataframe(filtered_df, use_container_width=True, height=400)
    
    st.markdown(f"**Showing {len(filtered_df)} of {len(df)} relationships**")
    
    # Explanation
    with st.expander("ℹ️ Mapping Type Explanations"):
        st.markdown("""
        - **Mitigates**: The NIST control prevents or reduces the effectiveness of the MITRE technique
        - **Detects**: The NIST control can identify when the MITRE technique is being executed
        - **Responds**: The NIST control provides mechanisms to respond to or recover from the MITRE technique
        """)

def show_knowledge_paths(paths_data):
    """Knowledge Paths view"""
    st.header("🗺️ GraphRAG Knowledge Paths")
    
    st.info("Displaying pre-computed knowledge graph reasoning paths (N=5)")
    
    knowledge_paths = paths_data['knowledge_paths']
    
    # Path selector
    path_options = [f"{p['path_id']}: {p['source']} → {p['target']}" for p in knowledge_paths]
    selected_path_idx = st.selectbox("Select Knowledge Path", range(len(path_options)), format_func=lambda x: path_options[x])
    
    selected_path = knowledge_paths[selected_path_idx]
    
    # Display path details
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Path Details")
        st.markdown(f"**Source**: `{selected_path['source']}`")
        st.markdown(f"**Target**: `{selected_path['target']}`")
        st.markdown(f"**Relationship**: `{selected_path['relationship']}`")
        
        st.markdown("#### Reasoning")
        st.write(selected_path['reasoning'])
        
        st.markdown("#### Path Structure")
        for i, node in enumerate(selected_path['path']):
            st.markdown(f"{i+1}. **{node['label']}** (`{node['type']}`)")
            st.text(f"   └─ {node['node']}")
    
    with col2:
        st.subheader("Path Statistics")
        st.metric("Path Length", len(selected_path['path']))
        st.metric("Node Types", len(set(n['type'] for n in selected_path['path'])))
        
        # Visualize path as network
        st.markdown("#### Path Flow")
        for i in range(len(selected_path['path']) - 1):
            current = selected_path['path'][i]
            next_node = selected_path['path'][i + 1]
            st.markdown(f"```\n{current['label']}\n   ↓\n{next_node['label']}\n```")

def show_about():
    """About page"""
    st.header("ℹ️ About IMGO")
    
    st.markdown("""
    ## Project Information
    
    **IMGO** (Intelligent Multi-Framework Integrated Ontology-based GraphRAG) is a **demonstration version** 
    of the ISGO v2.1 research project, created for public showcase purposes.
    
    ### Version Information
    - **Demo Version**: v1.0.0-alpha (Public)
    - **Base Project**: ISGO v2.1 (Private Research)
    - **Sample Size**: N=10 per dataset
    - **Purpose**: Skydeck showcase demonstration
    
    ### Key Features (Demo)
    - ✅ Browse sample NIST SP 800-53 controls
    - ✅ Explore sample MITRE ATT&CK techniques
    - ✅ View AI RMF mappings
    - ✅ Examine NIST-MITRE relationships
    - ✅ Explore pre-computed knowledge paths
    
    ### Limitations (Demo)
    - ❌ Limited to sample data (N=10)
    - ❌ No real-time GraphRAG queries
    - ❌ No database integration (Neo4j/ChromaDB)
    - ❌ No LLM integration (GPT-4)
    - ❌ Static, pre-computed relationships only
    
    ### Full ISGO v2.1 Features
    
    The complete research version includes:
    - 🔬 Full datasets (N>10,000)
    - 🤖 Real-time GraphRAG with GPT-4
    - 📊 Neo4j graph database
    - 🎯 ChromaDB vector embeddings
    - 🔄 Multi-hop reasoning (up to 10 hops)
    - 📈 Real-time framework updates
    - 🔐 Advanced security features
    
    **Access to full version requires research collaboration agreement.**
    
    ### Technology Stack (Demo)
    - **Frontend**: Streamlit
    - **Language**: Python 3.12
    - **Data**: Pandas
    - **Visualization**: Plotly
    - **Deployment**: Docker
    
    ### Data Sources
    - **NIST SP 800-53 Rev. 5**: Public domain (US Government)
    - **MITRE ATT&CK Framework v14**: Free use (MITRE Corporation)
    - **NIST AI RMF 1.0**: Public domain (NIST)
    
    ### License
    - Demo code: MIT License
    - Data: Public domain / Fair use
    - Full ISGO v2.1: Proprietary (Research collaboration required)
    
    ### Status
    - **Publication**: Pre-publication (manuscript in preparation)
    - **DOI**: Not yet assigned
    - **Peer Review**: In progress
    
    ### Contact
    - **Project**: ISGO v2.1 (Caroline's Research Team)
    - **Demo**: IMGO v1.0.0-alpha
    - **Repository**: https://github.com/almanix00/IMGO
    
    ---
    
    **Note**: This is a demonstration version with limited functionality. 
    For research collaboration or access to the full ISGO v2.1 system, please contact the research team.
    """)

if __name__ == "__main__":
    main()
