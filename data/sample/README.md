# IMGO Sample Data (N=10)

## Overview

This directory contains **sample datasets (N=10)** for demonstrating IMGO capabilities. These are **representative subsets** from the full ISGO v2.1 project dataset.

## ⚠️ Important Notes

- **Sample Size**: N=10 per dataset (demonstration purposes only)
- **Full Dataset**: Not included (private research data)
- **Data Source**: Derived from Caroline's ISGO v2.1 project
- **Purpose**: Public demonstration for Skydeck showcase

## Dataset Files

### 1. `sample_nist_controls.csv`
- **Description**: NIST SP 800-53 security controls
- **Columns**: control_id, family, name, description, priority
- **Sample Size**: 10 controls
- **Source**: NIST SP 800-53 Rev. 5

### 2. `sample_mitre_techniques.csv`
- **Description**: MITRE ATT&CK techniques
- **Columns**: technique_id, tactic, name, description, platforms
- **Sample Size**: 10 techniques
- **Source**: MITRE ATT&CK Framework v14

### 3. `sample_ai_rmf_mapping.csv`
- **Description**: NIST AI RMF to NIST 800-53 mappings
- **Columns**: ai_rmf_function, ai_rmf_category, nist_control, description, risk_level
- **Sample Size**: 10 mappings
- **Source**: NIST AI RMF 1.0

### 4. `sample_nist_mitre_mapping.csv`
- **Description**: Mappings between NIST controls and MITRE techniques
- **Columns**: nist_control, mitre_technique, mapping_type, confidence, description
- **Sample Size**: 10 mappings
- **Source**: NIST-MITRE Cross-Reference

### 5. `sample_graphrag_paths.json`
- **Description**: Example knowledge graph paths
- **Format**: JSON with nested path structures
- **Sample Size**: 5 reasoning paths
- **Source**: Manually curated examples

## Data Dictionary

Refer to `docs/data_dictionary.md` for detailed column descriptions.

## Usage

```python
import pandas as pd

# Load sample data
nist_controls = pd.read_csv('data/sample/sample_nist_controls.csv')
mitre_techniques = pd.read_csv('data/sample/sample_mitre_techniques.csv')
ai_rmf_mapping = pd.read_csv('data/sample/sample_ai_rmf_mapping.csv')
nist_mitre_mapping = pd.read_csv('data/sample/sample_nist_mitre_mapping.csv')

import json
with open('data/sample/sample_graphrag_paths.json', 'r') as f:
    graphrag_paths = json.load(f)
```

## Limitations

- **Not Production-Ready**: Sample data for demonstration only
- **Incomplete Coverage**: Does not represent full framework coverage
- **Simplified Relationships**: Complex multi-hop reasoning requires full dataset
- **No Real-Time Updates**: Static snapshot from research project

## License

Data compiled from public sources:
- NIST SP 800-53: Public domain (US Government)
- MITRE ATT&CK: Free for use (MITRE Corporation)
- AI RMF: Public domain (NIST)

Mappings and derivations: © 2026 Caroline's Research Team

## Contact

For access to full datasets or research collaboration:
- Project: ISGO v2.1 (Private)
- Demo: IMGO v1.0.0-alpha (Public)
- Status: Pre-publication (DOI pending)
