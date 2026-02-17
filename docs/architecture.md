# IMGO System Architecture

## Overview

**IMGO (Intelligent Multi-Framework Integrated Ontology-based GraphRAG)** is a simplified demonstration version of the ISGO v2.1 research project, designed for public showcase at Skydeck.

---

## Architecture Comparison

### ISGO v2.1 (Full Research Version - Private)

```
┌─────────────────────────────────────────────────────┐
│                   ISGO v2.1                         │
├─────────────────────────────────────────────────────┤
│  Frontend: React + TypeScript + Material-UI        │
│  Backend: FastAPI + Python                         │
│  GraphRAG: Microsoft GraphRAG + LangChain          │
│  Vector DB: ChromaDB / Milvus                      │
│  Graph DB: Neo4j                                   │
│  LLM: GPT-4 / Azure OpenAI                         │
│  Data: Full datasets (N>10,000)                    │
│  Features: Multi-hop reasoning, real-time updates  │
└─────────────────────────────────────────────────────┘
```

### IMGO v1.0.0-alpha (Demo Version - Public)

```
┌─────────────────────────────────────────────────────┐
│                IMGO v1.0.0-alpha                    │
├─────────────────────────────────────────────────────┤
│  Frontend: Streamlit (Single-page app)            │
│  Backend: Embedded in Streamlit                    │
│  GraphRAG: Simulated (pre-computed paths)         │
│  Vector DB: Not included                           │
│  Graph DB: Not included                            │
│  LLM: Not included                                 │
│  Data: Sample datasets (N=10)                      │
│  Features: Static demonstration, visualization     │
└─────────────────────────────────────────────────────┘
```

---

## IMGO Demo Architecture

### System Components

```
┌──────────────────────────────────────────────┐
│         User Browser                         │
└────────────────┬─────────────────────────────┘
                 │ HTTP (Port 8501)
                 ▼
┌──────────────────────────────────────────────┐
│      Streamlit Dashboard                     │
│  ┌────────────────────────────────────────┐ │
│  │  UI Components:                        │ │
│  │  - Header & Navigation                 │ │
│  │  - Data Browser                        │ │
│  │  - Relationship Viewer                 │ │
│  │  - Path Visualizer                     │ │
│  │  - Statistics Dashboard                │ │
│  └────────────────────────────────────────┘ │
└──────────────┬───────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────┐
│      Data Layer (Local Files)                │
│  ┌────────────────────────────────────────┐ │
│  │  CSV Files:                            │ │
│  │  - sample_nist_controls.csv            │ │
│  │  - sample_mitre_techniques.csv         │ │
│  │  - sample_ai_rmf_mapping.csv           │ │
│  │  - sample_nist_mitre_mapping.csv       │ │
│  │                                         │ │
│  │  JSON Files:                           │ │
│  │  - sample_graphrag_paths.json          │ │
│  └────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘
```

---

## Technology Stack

### Core Framework
- **Streamlit 1.31.0**: Interactive web application framework
- **Python 3.12**: Programming language

### Data Processing
- **Pandas 2.2.0**: Data manipulation and analysis
- **NumPy 1.26.4**: Numerical computing

### Visualization
- **Plotly 5.18.0**: Interactive charts and graphs

### Utilities
- **python-dotenv 1.0.1**: Environment configuration

---

## Application Structure

### Directory Layout

```
/home/user/webapp/
├── apps/
│   └── demo_dashboard.py          # Main Streamlit application
├── data/
│   └── sample/                    # Sample datasets (N=10)
│       ├── README.md
│       ├── *.csv                  # Tabular data
│       └── *.json                 # Graph paths
├── docs/
│   ├── architecture.md            # This file
│   └── data_dictionary.md         # Data specifications
├── tests/                         # Future: unit tests
├── Dockerfile                     # Container definition
├── docker-compose.yml             # Service orchestration
├── requirements.txt               # Python dependencies
└── README.md                      # Project overview
```

### Application Flow

```
1. User Access
   └─> http://localhost:8501
       │
2. Streamlit Initialization
   └─> Load environment configuration
   └─> Initialize data loader
       │
3. Data Loading
   └─> Read CSV files (Pandas)
   └─> Parse JSON paths
   └─> Cache in Streamlit session
       │
4. User Interaction
   └─> Select dataset to view
   └─> Filter/search data
   └─> View relationships
   └─> Explore knowledge paths
       │
5. Visualization
   └─> Generate Plotly charts
   └─> Display tables
   └─> Show path diagrams
```

---

## Key Features (Demo Version)

### ✅ Included

1. **Data Browser**
   - View NIST controls
   - View MITRE techniques
   - View AI RMF mappings
   - View NIST-MITRE relationships

2. **Relationship Viewer**
   - Filter by mapping type
   - Sort by confidence
   - Search functionality

3. **Path Visualizer**
   - Display knowledge graph paths
   - Show reasoning explanations
   - Interactive path exploration

4. **Statistics Dashboard**
   - Dataset summaries
   - Relationship counts
   - Distribution charts

### ❌ Not Included (Full Version Only)

1. **GraphRAG Integration**
   - Real-time LLM queries
   - Dynamic path generation
   - Multi-hop reasoning

2. **Database Systems**
   - Neo4j graph database
   - ChromaDB vector store
   - Persistent storage

3. **Advanced Features**
   - User authentication
   - Data upload/management
   - Real-time updates
   - API endpoints

---

## Deployment Architecture

### Docker Container

```
┌─────────────────────────────────────────┐
│     Docker Container: imgo-demo         │
├─────────────────────────────────────────┤
│  Base: python:3.12-slim                 │
│  Workdir: /app                          │
│  Exposed: 8501                          │
│                                         │
│  Volumes:                               │
│  - ./apps → /app/apps                   │
│  - ./data → /app/data                   │
│  - ./docs → /app/docs                   │
│                                         │
│  Command:                               │
│  streamlit run apps/demo_dashboard.py   │
└─────────────────────────────────────────┘
```

### Health Check

- **Endpoint**: `http://localhost:8501/_stcore/health`
- **Interval**: 30 seconds
- **Timeout**: 10 seconds
- **Retries**: 3

---

## Performance Considerations

### Optimization for Demo

1. **Data Size**: Limited to N=10 per dataset
2. **Caching**: Streamlit session state caching
3. **No External Calls**: All data loaded locally
4. **Lightweight**: Minimal dependencies

### Resource Requirements

- **Memory**: ~200 MB
- **CPU**: Minimal (single-threaded)
- **Storage**: <50 MB
- **Network**: None (except initial access)

---

## Security Considerations

### Demo Environment

- ⚠️ **No Authentication**: Open access for demo
- ⚠️ **No Encryption**: HTTP only (not HTTPS)
- ⚠️ **No Data Validation**: Read-only static files
- ⚠️ **No Rate Limiting**: Single-user demonstration

### Production Recommendations (Future)

- ✅ Add user authentication (OAuth2)
- ✅ Enable HTTPS/TLS
- ✅ Implement input validation
- ✅ Add rate limiting
- ✅ Regular security audits

---

## Limitations

### Technical Limitations

1. **Static Data**: No real-time updates
2. **No AI**: Pre-computed paths only
3. **Limited Scale**: N=10 samples
4. **Single User**: No concurrent access optimization

### Functional Limitations

1. **No Custom Queries**: Fixed dataset exploration
2. **No Data Upload**: Read-only interface
3. **No Export**: No data download features
4. **No Persistence**: No session saving

---

## Future Roadmap

### Potential Enhancements (If Full Version Released)

1. **Phase 1**: Add more sample data (N=50)
2. **Phase 2**: Implement basic GraphRAG demo
3. **Phase 3**: Add Neo4j Lite for visualization
4. **Phase 4**: Enable custom query input

**Note**: Full ISGO v2.1 features require research collaboration agreement.

---

## References

- **Streamlit Documentation**: https://docs.streamlit.io/
- **NIST Frameworks**: https://www.nist.gov/
- **MITRE ATT&CK**: https://attack.mitre.org/

---

**Version**: 1.0.0-alpha  
**Last Updated**: 2026-02-17  
**Status**: Demo Architecture Only
