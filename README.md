# IMGO - Intelligent Multi-Framework Integrated Ontology-based GraphRAG

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0--alpha-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-red)
![Docker](https://img.shields.io/badge/docker-ready-2496ed)
![Status](https://img.shields.io/badge/status-demo-yellow)
[![BFO Compliant](https://img.shields.io/badge/BFO-ISO%2FIEC%2021838--2-blue)](https://basic-formal-ontology.org/)
[![Ontology](https://img.shields.io/badge/Ontology-Standardized%20via%20BFO-success)](https://github.com/almanix00/ISGO)

**Public demonstration version of ISGO v2.1 research project**

[Quick Start](#quick-start) • [Features](#features) • [Documentation](#documentation) • [License](#license)

</div>

---

## ⚠️ Important Notice

This is a **demonstration version** with **sample data (N=10)** for public showcase purposes only.

- **Full Version**: ISGO v2.1 (private research project)
- **Demo Version**: IMGO v1.0.0-alpha (public showcase)
- **Data**: Sample datasets only (N=10 per dataset)
- **Purpose**: Skydeck demonstration

**Full ISGO v2.1 system available through research collaboration.**

---

## 📋 Overview

**IMGO** (Intelligent Multi-Framework Integrated Ontology-based GraphRAG) demonstrates the integration of multiple cybersecurity frameworks using simplified GraphRAG concepts:

- **NIST SP 800-53**: Security and privacy controls
- **MITRE ATT&CK**: Adversarial tactics and techniques
- **NIST AI RMF**: AI Risk Management Framework

### What This Demo Shows

✅ Browse security controls and attack techniques  
✅ Explore framework mappings and relationships  
✅ Visualize pre-computed knowledge paths  
✅ Interactive data exploration dashboard  
✅ **View BFO compliance and ontology standardization details**  

### What's Not Included (Full Version Only)

❌ Real-time GraphRAG with LLM integration  
❌ Complete datasets (N>10,000)  
❌ Neo4j graph database  
❌ ChromaDB vector embeddings  
❌ Multi-hop reasoning engine  
❌ Dynamic query processing  

---

## 🚀 Quick Start

### Prerequisites

- Docker Engine 20.10+
- Docker Compose 2.0+
- 2 GB free disk space

### Installation

```bash
# Clone repository
git clone https://github.com/almanix00/IMGO.git
cd IMGO

# Build and start
docker-compose up --build -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

### Access

Open your browser: **http://localhost:8501**

### Stop

```bash
docker-compose down
```

---

## 📊 Features

### 1. Data Browser

Explore sample datasets focused on **SR-3 Supply Chain Risk Management**:
- **NIST Controls**: 9 controls (SR-3, SR-6, SA-12 focus) with FKGL scores 17.3-24.5
- **MITRE Techniques**: 10 techniques (T1195 Supply Chain Compromise focus)
- **AI RMF Requirements**: 5 AI governance requirements
- **Mappings**: 10 NIST-MITRE relationships with confidence scores 0.79-0.94

### 2. Interactive Dashboard

- Filter and search functionality
- Sortable tables
- Distribution charts
- Relationship visualizations

### 3. Knowledge Paths

Explore 5 pre-computed **SR-3 focused** reasoning paths showing:
- Supply chain compromise scenarios (SolarWinds-style attacks)
- Multi-control mitigation strategies
- AI supply chain risk considerations
- Confidence scores and inference paths

### 4. Statistics

View dataset summaries and distributions:
- FKGL readability scores (17.3-24.5, graduate level)
- Control family distributions (SR, AC, IA, AU, SI, CM, RA)
- MITRE tactic classifications
- Mapping confidence distributions

### 5. BFO Compliance Information

View **ISGO v3.0** BFO standardization details:
- **Sidebar Badge**: ISO/IEC 21838-2 compliance status and coverage metrics
- **About Page**: Comprehensive BFO integration information including:
  - Ontology statistics (1,642 nodes, 41,911 relationships)
  - BFO class mappings (NISTControl, MITRETechnique, AIRMFRequirement)
  - BFO relationship properties (realized_in, is_about, participates_in)
  - Benefits of BFO standardization
  - Links to ISGO v3.0 repository and documentation

---

## 📁 Project Structure

```
/home/user/webapp/
├── apps/
│   └── demo_dashboard.py          # Main Streamlit app (with BFO UI)
├── data/
│   └── sample/                    # Sample datasets (SR-3 focused)
│       ├── README.md
│       ├── nist_controls_sample.csv      # N=9 (FKGL: 17.3-24.5)
│       ├── mitre_techniques_sample.csv   # N=10 (T1195 focused)
│       ├── ai_rmf_sample.csv             # N=5 (GOVERN/MAP)
│       ├── mapping_sample.csv            # N=10 (Confidence: 0.79-0.94)
│       └── graphrag_paths_sample.json    # N=5 (SR-3 scenarios)
├── neo4j_bfo/                     # BFO Integration Scripts
│   ├── schema.cypher              # Complete BFO-compliant schema
│   ├── 01_add_bfo_labels.cypher   # Add BFO labels to nodes
│   ├── 02_add_bfo_relationship_properties.cypher  # Add BFO properties
│   ├── 03_verify_bfo_integration.cypher           # Verification queries
│   ├── 00_update_consensus_validation.cypher      # Consensus mappings
│   └── integration_test.cypher    # Integration tests
├── docs/
│   ├── architecture.md            # System architecture
│   └── data_dictionary.md         # Data specifications
├── Dockerfile                     # Container definition
├── docker-compose.yml             # Service orchestration
├── requirements.txt               # Python dependencies
├── .env.example                   # Configuration template
└── README.md                      # This file
```

---
```

---

## 🛠️ Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Framework | Streamlit | 1.31.0 |
| Language | Python | 3.12 |
| Data | Pandas | 2.2.0 |
| Visualization | Plotly | 5.18.0 |
| Container | Docker | 20.10+ |

---

## 📖 Documentation

### User Guides

- [Architecture Overview](docs/architecture.md)
- [Data Dictionary](docs/data_dictionary.md)
- [Sample Data README](data/sample/README.md)

### Data Sources

| Framework | Version | Source | License |
|-----------|---------|--------|---------|
| NIST SP 800-53 | Rev. 5 | [NIST](https://csrc.nist.gov/) | Public Domain |
| MITRE ATT&CK | v14 | [MITRE](https://attack.mitre.org/) | Free Use |
| NIST AI RMF | 1.0 | [NIST](https://www.nist.gov/itl/ai-risk-management-framework) | Public Domain |

---

## 🏛️ Standardized via BFO (Basic Formal Ontology)

**ISGO v3.0** is now **ISO/IEC 21838-2 compliant**, integrating the Basic Formal Ontology (BFO) standard for robust, interoperable ontology design.

### BFO Integration Overview

- **Standard**: ISO/IEC 21838-2 (Basic Formal Ontology)
- **Status**: Production-ready, deployed on GitHub main branch
- **Repository**: [ISGO v3.0](https://github.com/almanix00/ISGO)

### Ontology Statistics

| Metric | Count | BFO Coverage |
|--------|-------|--------------|
| **Total Nodes** | 1,642 | 100% BFO-categorized |
| **Total Relationships** | 41,911 | 100% BFO property-mapped |
| **MITIGATES** | 20,658 | `realized_in` |
| **ADDRESSES/RELATED_TO/BELONGS_TO** | 21,219 | `is_about` |
| **USES** | 34 | `participates_in` |
| **Consensus Mappings** | 1,567 | Cross-validated (DeepSeek-V3 + GPT-4o) |

### BFO Class Mappings

#### Upper-Level Classes

```
Continuant (계속체 - time-independent entities)
├─ IndependentContinuant (독립 계속체)
├─ SpecificallyDependentContinuant (특정 의존 계속체)
└─ GenericallyDependentContinuant (일반 의존 계속체)
   └─ InformationContentEntity (정보 내용 개체)

Occurrent (발생체 - time-dependent entities)
└─ Process (과정)
```

#### Domain Class Mappings

- **NISTControl** → `Continuant:InformationContentEntity`
- **AIRMFRequirement** → `Continuant:InformationContentEntity`
- **MITRETechnique** → `Occurrent:Process`
- **Asset** → `IndependentContinuant`
- **System** → `IndependentContinuant`

### BFO Relationship Properties

| Relationship | BFO Property | Example |
|--------------|--------------|---------|
| MITIGATES | `realized_in` | (SR-3)-[:MITIGATES {bfo_type: "realized_in"}]->(T1195) |
| ADDRESSES/RELATED_TO/BELONGS_TO | `is_about` | (SR-3)-[:RELATED_TO {bfo_type: "is_about"}]->(SA-8) |
| USES | `participates_in` | (Asset)-[:USES {bfo_type: "participates_in"}]->(T1195) |

### Neo4j Cypher Scripts

All BFO integration scripts are available in the [`neo4j_bfo/`](neo4j_bfo/) directory:

- **[schema.cypher](neo4j_bfo/schema.cypher)**: Complete BFO-compliant schema
- **[01_add_bfo_labels.cypher](neo4j_bfo/01_add_bfo_labels.cypher)**: Add BFO labels to nodes
- **[02_add_bfo_relationship_properties.cypher](neo4j_bfo/02_add_bfo_relationship_properties.cypher)**: Add BFO properties to relationships
- **[03_verify_bfo_integration.cypher](neo4j_bfo/03_verify_bfo_integration.cypher)**: Verify BFO compliance
- **[00_update_consensus_validation.cypher](neo4j_bfo/00_update_consensus_validation.cypher)**: Update consensus mappings
- **[integration_test.cypher](neo4j_bfo/integration_test.cypher)**: Comprehensive integration tests

### Key Commits

- **BFO Integration Merge**: [1f77510](https://github.com/almanix00/ISGO/commit/1f77510)
- **BFO Compliance Declaration**: [9b2dfab](https://github.com/almanix00/ISGO/commit/9b2dfab)

### Benefits of BFO Standardization

✅ **Interoperability**: ISO/IEC 21838-2 standard ensures compatibility with other BFO-compliant ontologies  
✅ **Formal Semantics**: Clear, machine-readable definitions of entities and relationships  
✅ **Reasoning Support**: Enhanced capability for automated reasoning and inference  
✅ **Quality Assurance**: 100% coverage ensures all entities are properly categorized  

---

## 🔬 Research Context

### ISGO v2.1 (Full Research Project)

- **Status**: Active research project
- **Scope**: Complete cybersecurity framework integration
- **Data**: Full datasets (N>10,000)
- **Features**: Real-time GraphRAG, Neo4j, ChromaDB, LLM integration
- **Access**: Research collaboration required

### IMGO v1.0.0-alpha (This Demo)

- **Status**: Public demonstration
- **Scope**: Sample data showcase
- **Data**: Limited samples (N=10)
- **Features**: Static visualization and exploration
- **Access**: Open source (MIT License)

### Publication Status

- **Manuscript**: In preparation
- **Peer Review**: Pending submission
- **DOI**: Will be assigned upon publication
- **Expected**: 2026 Q2-Q3

---

## 🔒 Data Privacy

### Sample Data

## 📊 Sample Data

This repository includes **sample data (N=10)** for demonstration purposes:

| Dataset | Count | Description |
|---------|-------|-------------|
| NIST Controls | 9 | SR-3 (Supply Chain Risk Management) centered |
| MITRE Techniques | 10 | T1195 (Supply Chain Compromise) focused |
| NIST-MITRE Mappings | 10 | Deterministic relationships (confidence 0.79-0.94) |
| AI RMF Requirements | 5 | GOVERN, MAP categories |
| GraphRAG Paths | 5 | SR-3 supply chain scenarios |

### Representative Scenario: SR-3 Supply Chain Risk

The sample data demonstrates **supply chain security governance**, showing how NIST SP 800-53 controls (SR-3, SR-6, SA-12) mitigate supply chain compromise attacks (MITRE T1195) through:
- Supplier risk assessments
- Protection mechanisms
- Risk management strategies

### Data Source & Privacy

**Sample Data Characteristics**:
- ✅ Derived from **public standards** (NIST SP 800-53 Rev. 5, MITRE ATT&CK v14)
- ✅ **Real FKGL scores** (17.3-24.5) from actual NIST documentation
- ✅ **Safe for public distribution** (N=10, no sensitive information)
- ✅ Representative of research methodology

**Full Dataset (Not Included)**:

The complete ISGO v2.1 research dataset contains:
- **1,642 nodes** (324 NIST base controls → 1,196 granular nodes; 1,316 MITRE techniques → 356 validated mappings)
- **41,911 semantic relationships** (20,104 MITIGATES edges, 215 ALIGNS_WITH edges)
- ChromaDB vector embeddings for GraphRAG reasoning

**Availability**: The full dataset is **not publicly available** due to:
- Proprietary research methodology
- Ongoing academic publication process
- Data use agreements with institutional review

**For Academic Research**: Please contact the author for collaboration opportunities. Full dataset access may be granted upon:
- Formal research proposal
- Institutional review board approval
- Data use agreement signature

---

**Related Projects**:
- 📚 Base Research: ISGO v2.1 (Private Repository)
- 🎓 Institution: [Caroline University]


---

## 🤝 Contributing

This is a demonstration project. Contributions to the demo are welcome:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/demo-enhancement`)
3. Commit changes (`git commit -m 'Add demo feature'`)
4. Push to branch (`git push origin feature/demo-enhancement`)
5. Open Pull Request

**Note**: Contributions to full ISGO v2.1 require research collaboration.

---

## 📄 License

### Demo Code (This Repository)

MIT License - See [LICENSE](LICENSE) file

### Data Sources

- NIST Publications: Public Domain (US Government)
- MITRE ATT&CK: Free use with attribution
- Derived mappings: © 2026 Research Team

### Full ISGO v2.1

Proprietary - Research collaboration required

---

## 🐛 Troubleshooting

### Common Issues

**Port 8501 already in use**
```bash
# Stop conflicting service or change port in docker-compose.yml
docker-compose down
docker-compose up -d
```

**Container won't start**
```bash
# Check logs
docker-compose logs imgo-demo

# Rebuild from scratch
docker-compose down -v
docker-compose up --build -d
```

**Data not loading**
```bash
# Verify data files exist
ls -la data/sample/

# Check file permissions
chmod 644 data/sample/*.csv data/sample/*.json
```

---

## 📞 Contact

### For Demo Questions

- **GitHub Issues**: [Create an issue](https://github.com/almanix00/IMGO/issues)
- **Repository**: [almanix00/IMGO](https://github.com/almanix00/IMGO)

### For Research Collaboration

- **Project**: ISGO v2.1
- **Principal Investigator**: Caroline's Research Team
- **Access**: By invitation/collaboration agreement only

---

## 🙏 Acknowledgments

- **NIST**: For public cybersecurity frameworks
- **MITRE Corporation**: For ATT&CK Framework
- **Streamlit**: For rapid prototyping framework
- **Research Team**: Caroline and collaborators

---

## ⚖️ Disclaimer

This is a **demonstration project** with **limited functionality**. It does not represent:
- Production-ready software
- Complete research findings
- Validated security recommendations
- Operational security guidance

For production cybersecurity implementations, consult official framework documentation and security professionals.

---

<div align="center">

**IMGO v1.0.0-alpha** | **Demo Version** | **2026**

[⬆ Back to Top](#imgo---intelligent-multi-framework-integrated-ontology-based-graphrag)

</div>
