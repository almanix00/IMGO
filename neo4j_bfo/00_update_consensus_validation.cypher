// ==========================================
// Update Consensus MITIGATES Relationships
// Cross-validated by DeepSeek-V3 + GPT-4o
// ==========================================

// Update 1,567 consensus mappings (7.79% of 20,104 total)
LOAD CSV WITH HEADERS FROM 'file:///consensus_pairs_for_neo4j.csv' AS row
MATCH (c:NISTControl {control_id: row.nist_control_id})
MATCH (t:MITRETechnique {technique_id: row.mitre_technique_id})
MATCH (c)-[r:MITIGATES]->(t)
SET 
  r.mapping_source = "cross-validated (DeepSeek + GPT-4o)",
  r.confidence = 100,
  r.is_consensus = true,
  r.validation_date = datetime()
RETURN count(r) as updated_relationships;
// Expected: 1,567 relationships

// Verification query
MATCH ()-[r:MITIGATES {is_consensus: true}]->()
RETURN count(r) as consensus_count, 
       avg(r.confidence) as avg_confidence;
// Expected: 1,567, 100.0

// Statistics by source
MATCH ()-[r:MITIGATES]->()
RETURN r.mapping_source, count(r) as count, avg(r.confidence) as avg_conf
ORDER BY count DESC;
