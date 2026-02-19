// ==========================================
// ISGO v3.0 - Integration Tests
// ISO/IEC 21838-2 Compliance Verification
// ==========================================

// Test 1: SR-3 to MITRE path via BFO
MATCH (c:NISTControl:InformationContentEntity {control_id: "SR-3"})
      -[r:MITIGATES {bfo_type: "realized_in"}]->
      (t:MITRETechnique:Process)
RETURN c.control_id, t.technique_id, r.bfo_type, r.confidence
LIMIT 5;

// Test 2: Multi-hop BFO reasoning
MATCH path = (c1:NISTControl:InformationContentEntity {control_id: "SR-3"})
             -[r1:RELATED_TO {bfo_type: "is_about"}]->
             (c2:NISTControl:InformationContentEntity)
             -[r2:MITIGATES {bfo_type: "realized_in"}]->
             (t:MITRETechnique:Process)
RETURN c1.control_id, c2.control_id, t.technique_id, 
       r1.bfo_type, r2.bfo_type
LIMIT 10;

// Test 3: BFO class hierarchy verification
MATCH (n)
WHERE n:Continuant OR n:Occurrent
RETURN 
  CASE 
    WHEN n:Continuant THEN "Continuant"
    WHEN n:Occurrent THEN "Occurrent"
  END as upper_class,
  labels(n) as all_labels,
  count(n) as count
ORDER BY upper_class;

// Test 4: Consensus mappings verification
MATCH ()-[r:MITIGATES {is_consensus: true, bfo_type: "realized_in"}]->()
RETURN count(r) as consensus_count, 
       avg(r.confidence) as avg_confidence,
       r.mapping_source as source
LIMIT 1;
// Expected: 1,567, 100.0, "cross-validated (DeepSeek + GPT-4o)"

// Test 5: AI RMF integration
MATCH (a:AIRMFRequirement:InformationContentEntity)
      -[r:RELATED_TO {bfo_type: "is_about"}]->
      (c:NISTControl:InformationContentEntity)
RETURN a.requirement_id, c.control_id, r.bfo_type
LIMIT 5;

// Test 6: Full coverage check
MATCH (n) 
RETURN 
  count(n) as total_nodes,
  count(CASE WHEN n:Continuant OR n:Occurrent THEN 1 END) as bfo_nodes,
  100.0 * count(CASE WHEN n:Continuant OR n:Occurrent THEN 1 END) / count(n) as coverage_percent;
// Expected: 1,642, 1,642, 100.0

// Test 7: Relationship property coverage
MATCH ()-[r]->()
RETURN 
  count(r) as total_rels,
  count(CASE WHEN r.bfo_type IS NOT NULL THEN 1 END) as bfo_rels,
  100.0 * count(CASE WHEN r.bfo_type IS NOT NULL THEN 1 END) / count(r) as coverage_percent;
// Expected: 41,911, 41,911, 100.0

// Test 8: Performance test - SR-3 GraphRAG query
MATCH (c:NISTControl:InformationContentEntity {control_id: "SR-3"})
CALL {
  WITH c
  MATCH (c)-[r1:MITIGATES {bfo_type: "realized_in"}]->(t:MITRETechnique:Process)
  RETURN collect(DISTINCT t.technique_id) as mitre_techniques
}
CALL {
  WITH c
  MATCH (c)-[r2:RELATED_TO {bfo_type: "is_about"}]->(c2:NISTControl:InformationContentEntity)
  RETURN collect(DISTINCT c2.control_id) as related_controls
}
RETURN 
  c.control_id,
  size(mitre_techniques) as mitre_count,
  size(related_controls) as nist_count,
  mitre_techniques[0..3] as sample_mitre,
  related_controls[0..3] as sample_nist;
// Expected: SR-3, 5, 21, [T1195, T1554, ...], [SA-8, SA-10, ...]
