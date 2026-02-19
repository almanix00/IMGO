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
import numpy as np
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
        color: #000000 !important;
    }
    .warning-box * {
        color: #000000 !important;
    }
    .warning-box strong {
        color: #000000 !important;
        font-weight: bold;
    }
    /* Ensure all Streamlit info/warning elements have black text */
    div[data-testid="stMarkdownContainer"] p {
        color: inherit;
    }
    .stAlert {
        color: #000000 !important;
    }
    .stAlert * {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load all sample datasets"""
    try:
        nist_controls = pd.read_csv(DATA_PATH / "nist_controls_sample.csv")
        mitre_techniques = pd.read_csv(DATA_PATH / "mitre_techniques_sample.csv")
        ai_rmf_mapping = pd.read_csv(DATA_PATH / "ai_rmf_sample.csv")
        nist_mitre_mapping = pd.read_csv(DATA_PATH / "mapping_sample.csv")
        
        with open(DATA_PATH / "graphrag_paths_sample.json", 'r') as f:
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
    st.sidebar.markdown(
        f"""
        <div style='background-color: #2e3949; padding: 1rem; border-radius: 0.5rem; color: #ffffff;'>
            <p style='margin: 0; color: #ffffff;'><strong style='color: #4da6ff;'>Version:</strong> {VERSION}</p>
            <p style='margin: 0.5rem 0 0 0; color: #ffffff;'><strong style='color: #4da6ff;'>Sample Size:</strong> N=10 per dataset</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # BFO Compliance Badge
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🏛️ BFO Compliance")
    st.sidebar.markdown(
        """
        <div style='background-color: #1e3a5f; padding: 0.8rem; border-radius: 0.5rem; color: #ffffff;'>
            <p style='margin: 0; color: #ffffff; font-size: 0.85rem;'>
                <strong style='color: #4da6ff;'>Standard:</strong> ISO/IEC 21838-2
            </p>
            <p style='margin: 0.3rem 0 0 0; color: #ffffff; font-size: 0.85rem;'>
                <strong style='color: #4da6ff;'>Status:</strong> ISGO v3.0 Certified
            </p>
            <p style='margin: 0.3rem 0 0 0; color: #ffffff; font-size: 0.85rem;'>
                <strong style='color: #4da6ff;'>Coverage:</strong> 100% (1,642 nodes)
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
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
        st.metric("Knowledge Paths", len(data['graphrag_paths']))
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("NIST Control Families")
        family_counts = data['nist_controls']['family'].value_counts()
        fig = px.pie(
            values=family_counts.values,
            names=family_counts.index,
            title="Distribution by Family",
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
    
    # FKGL Score Distribution
    st.subheader("NIST Control Readability (FKGL Scores)")
    
    # Manual histogram calculation for better control
    fkgl_scores = data['nist_controls']['fkgl_score'].values
    counts, bins = np.histogram(fkgl_scores, bins=5)
    bin_centers = (bins[:-1] + bins[1:]) / 2
    bin_labels = [f"{bins[i]:.1f}-{bins[i+1]:.1f}" for i in range(len(bins)-1)]
    
    fig = go.Figure(data=[
        go.Bar(
            x=bin_labels,
            y=counts,
            text=counts,
            textposition='outside',
            marker=dict(
                color='#1f77b4',
                line=dict(color='white', width=2)
            )
        )
    ])
    
    fig.update_layout(
        title="Flesch-Kincaid Grade Level Distribution",
        xaxis_title="FKGL Score Range (Readability Level)",
        yaxis_title="Count",
        showlegend=False,
        bargap=0.2,
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Show actual data points
    with st.expander("📊 View Individual FKGL Scores"):
        score_df = data['nist_controls'][['node_id', 'title', 'fkgl_score']].sort_values('fkgl_score')
        st.dataframe(score_df, use_container_width=True)

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
        # FKGL range filter
        fkgl_range = st.slider("FKGL Score Range", 
                               float(df['fkgl_score'].min()), 
                               float(df['fkgl_score'].max()),
                               (float(df['fkgl_score'].min()), float(df['fkgl_score'].max())))
    
    # Apply filters
    filtered_df = df.copy()
    if selected_family != 'All':
        filtered_df = filtered_df[filtered_df['family'] == selected_family]
    filtered_df = filtered_df[(filtered_df['fkgl_score'] >= fkgl_range[0]) & 
                              (filtered_df['fkgl_score'] <= fkgl_range[1])]
    
    # Display
    st.dataframe(filtered_df, use_container_width=True, height=400)
    
    st.markdown(f"**Showing {len(filtered_df)} of {len(df)} controls**")
    
    # FKGL explanation
    with st.expander("ℹ️ What is FKGL Score?"):
        st.markdown("""
        **Flesch-Kincaid Grade Level (FKGL)** measures text readability:
        - **8-10**: Easy to read (8th-10th grade level)
        - **11-12**: Average difficulty (High school level)
        - **13+**: Difficult (College level or higher)
        
        Lower scores indicate more accessible documentation.
        """)

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
    st.header("🤖 NIST AI RMF Requirements")
    
    st.info("Displaying AI Risk Management Framework requirements (N=10)")
    
    # Filters
    categories = ['All'] + sorted(df['category'].unique().tolist())
    selected_category = st.selectbox("Filter by Category", categories)
    
    # Apply filter
    filtered_df = df.copy()
    if selected_category != 'All':
        filtered_df = filtered_df[filtered_df['category'] == selected_category]
    
    # Display
    st.dataframe(filtered_df, use_container_width=True, height=400)
    
    st.markdown(f"**Showing {len(filtered_df)} of {len(df)} requirements**")

def show_nist_mitre_relationships(df):
    """NIST-MITRE Relationships view"""
    st.header("🔗 NIST-MITRE Relationship Mappings")
    
    st.info("Displaying relationships between NIST controls and MITRE techniques (N=10)")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        nist_controls = ['All'] + sorted(df['nist_control_id'].unique().tolist())
        selected_nist = st.selectbox("Filter by NIST Control", nist_controls)
    with col2:
        # Confidence slider
        conf_range = st.slider("Confidence Range", 0.0, 1.0, (0.0, 1.0))
    
    # Apply filters
    filtered_df = df.copy()
    if selected_nist != 'All':
        filtered_df = filtered_df[filtered_df['nist_control_id'] == selected_nist]
    filtered_df = filtered_df[(filtered_df['mapping_confidence'] >= conf_range[0]) & 
                              (filtered_df['mapping_confidence'] <= conf_range[1])]
    
    # Display
    st.dataframe(filtered_df, use_container_width=True, height=400)
    
    st.markdown(f"**Showing {len(filtered_df)} of {len(df)} relationships**")
    
    # Confidence distribution
    st.subheader("Mapping Confidence Distribution")
    
    # Manual histogram calculation
    conf_scores = df['mapping_confidence'].values
    counts, bins = np.histogram(conf_scores, bins=5)
    bin_labels = [f"{bins[i]:.2f}-{bins[i+1]:.2f}" for i in range(len(bins)-1)]
    
    fig = go.Figure(data=[
        go.Bar(
            x=bin_labels,
            y=counts,
            text=counts,
            textposition='outside',
            marker=dict(
                color='#2ca02c',
                line=dict(color='white', width=2)
            )
        )
    ])
    
    fig.update_layout(
        title="Distribution of Mapping Confidence Scores",
        xaxis_title="Confidence Score Range",
        yaxis_title="Count",
        showlegend=False,
        bargap=0.2,
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_knowledge_paths(paths_data):
    """Knowledge Paths view"""
    st.header("🗺️ GraphRAG Knowledge Paths")
    
    st.info("Displaying pre-computed knowledge graph reasoning paths (N=5)")
    
    # Path selector
    path_options = [f"{i+1}. {p['query']}" for i, p in enumerate(paths_data)]
    selected_path_idx = st.selectbox("Select Query", range(len(path_options)), format_func=lambda x: path_options[x])
    
    selected_path = paths_data[selected_path_idx]
    
    # Display path details
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Query Details")
        st.markdown(f"**Query**: {selected_path['query']}")
        
        st.markdown("#### Related NIST Controls")
        for control in selected_path['nist_controls']:
            st.markdown(f"- `{control}`")
        
        st.markdown("#### Related MITRE Techniques")
        for technique in selected_path['mitre_techniques']:
            st.markdown(f"- `{technique}`")
        
        st.markdown("#### Reasoning")
        st.info(selected_path['reasoning'])
    
    with col2:
        st.subheader("Path Metrics")
        st.metric("Confidence", f"{selected_path['confidence']:.2f}")
        st.metric("Path Length", selected_path['path_length'])
        st.metric("NIST Controls", len(selected_path['nist_controls']))
        st.metric("MITRE Techniques", len(selected_path['mitre_techniques']))
    
    st.markdown("---")
    
    # Overall statistics
    st.subheader("Overall Path Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_confidence = sum(p['confidence'] for p in paths_data) / len(paths_data)
        st.metric("Average Confidence", f"{avg_confidence:.2f}")
    with col2:
        avg_length = sum(p['path_length'] for p in paths_data) / len(paths_data)
        st.metric("Average Path Length", f"{avg_length:.1f}")
    with col3:
        st.metric("Total Paths", len(paths_data))

def show_about():
    """About page"""
    st.header("ℹ️ About IMGO")
    
    # BFO Section at the top
    st.markdown("## 🏛️ BFO Standardization (ISGO v3.0)")
    
    st.markdown("""
    **ISGO v3.0** is now **ISO/IEC 21838-2 compliant**, integrating the **Basic Formal Ontology (BFO)** 
    standard for robust, interoperable ontology design.
    """)
    
    # BFO Statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Nodes", "1,642", delta="100% BFO-categorized")
    with col2:
        st.metric("Total Relationships", "41,911", delta="100% BFO-mapped")
    with col3:
        st.metric("Consensus Mappings", "1,567", delta="Cross-validated")
    
    st.markdown("---")
    
    # BFO Details
    with st.expander("📊 BFO Integration Details", expanded=False):
        st.markdown("""
        ### BFO Class Mappings
        
        | Domain Class | BFO Class | Description |
        |--------------|-----------|-------------|
        | **NISTControl** | `Continuant:InformationContentEntity` | Security controls as information entities |
        | **MITRETechnique** | `Occurrent:Process` | Attack techniques as time-dependent processes |
        | **AIRMFRequirement** | `Continuant:InformationContentEntity` | AI governance requirements |
        | **Asset** | `IndependentContinuant` | Physical/logical assets |
        | **System** | `IndependentContinuant` | Information systems |
        
        ### BFO Relationship Properties
        
        | Relationship | BFO Property | Count | Description |
        |--------------|--------------|-------|-------------|
        | **MITIGATES** | `realized_in` | 20,658 | Controls realize mitigation in attack processes |
        | **ADDRESSES/RELATED_TO** | `is_about` | 21,219 | Entities describe other entities |
        | **USES** | `participates_in` | 34 | Entities participate in processes |
        
        ### Benefits of BFO Standardization
        
        ✅ **Interoperability**: ISO/IEC 21838-2 ensures compatibility with other ontologies  
        ✅ **Formal Semantics**: Clear, machine-readable entity definitions  
        ✅ **Reasoning Support**: Enhanced automated reasoning capabilities  
        ✅ **Quality Assurance**: 100% coverage ensures proper categorization  
        
        ### Reference
        - **Standard**: ISO/IEC 21838-2 (Basic Formal Ontology)
        - **ISGO Repository**: [https://github.com/almanix00/ISGO](https://github.com/almanix00/ISGO)
        - **Status**: Production-ready, deployed on main branch
        - **Commits**: [1f77510](https://github.com/almanix00/ISGO/commit/1f77510), [9b2dfab](https://github.com/almanix00/ISGO/commit/9b2dfab)
        """)
    
    st.markdown("---")
    
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
    - ✅ View AI RMF requirements
    - ✅ Examine NIST-MITRE relationships
    - ✅ Explore pre-computed knowledge paths
    - ✅ FKGL readability scores
    
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
