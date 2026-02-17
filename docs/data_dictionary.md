# IMGO Data Dictionary

## Overview

This document provides detailed descriptions of all data fields used in the IMGO demo.

---

## 1. NIST Controls (`sample_nist_controls.csv`)

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `control_id` | String | Unique NIST control identifier | AC-1, AU-2 |
| `family` | String | Control family name | Access Control, Audit and Accountability |
| `name` | String | Short control name | Access Control Policy and Procedures |
| `description` | String | Detailed control description | The organization develops and documents... |
| `priority` | String | Implementation priority | Critical, High, Medium, Low |

**Source**: NIST SP 800-53 Revision 5

---

## 2. MITRE Techniques (`sample_mitre_techniques.csv`)

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `technique_id` | String | MITRE ATT&CK technique ID | T1078, T1190 |
| `tactic` | String | ATT&CK tactic category | Initial Access, Credential Access |
| `name` | String | Technique name | Valid Accounts, Phishing |
| `description` | String | Technique description | Adversaries may obtain credentials... |
| `platforms` | String | Affected platforms (comma-separated) | Windows, Linux, macOS, Cloud |

**Source**: MITRE ATT&CK Framework v14

---

## 3. AI RMF Mapping (`sample_ai_rmf_mapping.csv`)

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `ai_rmf_function` | String | AI RMF core function | Govern, Map, Measure, Manage |
| `ai_rmf_category` | String | Specific category within function | Accountability, Risk Identification |
| `nist_control` | String | Mapped NIST 800-53 control | AC-1, AU-2 |
| `description` | String | Mapping rationale | AI governance requires access control... |
| `risk_level` | String | Associated risk level | Critical, High, Medium, Low |

**Source**: NIST AI Risk Management Framework 1.0

---

## 4. NIST-MITRE Mapping (`sample_nist_mitre_mapping.csv`)

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `nist_control` | String | NIST control ID | AC-3, IR-1 |
| `mitre_technique` | String | MITRE technique ID | T1078, T1486 |
| `mapping_type` | String | Relationship type | Mitigates, Detects, Responds |
| `confidence` | String | Mapping confidence level | Critical, High, Medium, Low |
| `description` | String | Relationship explanation | Access enforcement blocks unauthorized... |

**Mapping Types**:
- **Mitigates**: Control prevents or reduces technique effectiveness
- **Detects**: Control identifies technique execution
- **Responds**: Control provides recovery/response mechanisms

---

## 5. GraphRAG Paths (`sample_graphrag_paths.json`)

### Structure

```json
{
  "knowledge_paths": [
    {
      "path_id": "String - Unique path identifier",
      "source": "String - Starting node",
      "target": "String - Ending node",
      "relationship": "String - Overall relationship type",
      "path": [
        {
          "node": "String - Node identifier",
          "type": "String - Node type (Control, Technique, etc.)",
          "label": "String - Human-readable label"
        }
      ],
      "reasoning": "String - Explanation of the path logic"
    }
  ]
}
```

### Node Types

- **Control**: Security control (e.g., NIST 800-53)
- **Technique**: Attack technique (e.g., MITRE ATT&CK)
- **Framework**: Framework function (e.g., AI RMF)
- **Policy**: Policy domain or category
- **Process**: Security process or procedure
- **Category**: Classification or grouping
- **Asset**: System or resource type
- **Tactic**: High-level adversary goal

### Relationship Types

- **MITIGATES**: Control reduces technique risk
- **REQUIRES**: Entity depends on another
- **ADDRESSED_BY**: Problem solved by entity
- **IMPLEMENTS**: Concrete implementation of abstract concept
- **DETECTS**: Capability to identify activity
- **RESPONDS**: Capability to react to incident

---

## Data Quality Notes

### Sample Limitations

1. **Coverage**: N=10 samples per dataset
2. **Completeness**: Not all relationships represented
3. **Currency**: Snapshot from specific date
4. **Validation**: Manual curation, not automated

### Full Dataset Features (Not in Demo)

- Complete NIST 800-53 Rev. 5 controls (1000+ controls)
- Full MITRE ATT&CK matrix (600+ techniques)
- Comprehensive AI RMF mappings
- Multi-hop reasoning paths (up to 10 hops)
- Automated relationship extraction
- Real-time framework updates

---

## References

1. **NIST SP 800-53 Rev. 5**: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
2. **MITRE ATT&CK**: https://attack.mitre.org/
3. **NIST AI RMF**: https://www.nist.gov/itl/ai-risk-management-framework

---

**Version**: 1.0.0-alpha  
**Last Updated**: 2026-02-17  
**Status**: Sample Data Only
