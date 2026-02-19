// ==========================================
// ISGO v3.0 - Verify BFO Integration
// ISO/IEC 21838-2 Compliance - Step 3
// ==========================================

// Test 1: Count BFO-labeled nodes
MATCH (n:Continuant) RETURN "Continuant" as type, count(n) as count
UNION
MATCH (n:Occurrent) RETURN "Occurrent" as type, count(n) as count
UNION
MATCH (n:InformationContentEntity) RETURN "InformationContentEntity" as type, count(n) as count
UNION
MATCH (n:Process) RETURN "Process" as type, count(n) as count;
// Expected: Continuant ~1,215, Occurrent 356, ICE ~1,215, Process 356

// Test 2: Count BFO relationship properties
MATCH ()-[r]->()
WHERE r.bfo_type IS NOT NULL
RETURN r.bfo_type, count(r) as count
ORDER BY count DESC;
// Expected: is_about 21,219, realized_in 20,658, participates_in 34

// Test 3: Verify SR-3 BFO path
MATCH (c:NISTControl {control_id: "SR-3"})
OPTIONAL MATCH (c)-[r1:MITIGATES]->(t:MITRETechnique)
OPTIONAL MATCH (c)-[r2:RELATED_TO]->(c2:NISTControl)
RETURN 
  labels(c) as sr3_labels,
  r1.bfo_type as mitigates_bfo,
  r2.bfo_type as related_bfo,
  count(DISTINCT t) as mitre_count,
  count(DISTINCT c2) as related_controls
LIMIT 1;
// Expected: sr3_labels contains Continuant & InformationContentEntity
//           mitigates_bfo = "realized_in"
//           related_bfo = "is_about"

// Test 4: Total coverage check
MATCH (n) 
RETURN 
  count(n) as total_nodes,
  count(CASE WHEN n:Continuant OR n:Occurrent THEN 1 END) as bfo_categorized_nodes;
// Expected: total_nodes 1,642, bfo_categorized_nodes 1,642 (100%)

MATCH ()-[r]->()
RETURN
  count(r) as total_relationships,
  count(CASE WHEN r.bfo_type IS NOT NULL THEN 1 END) as bfo_mapped_relationships;
// Expected: total_relationships 41,911, bfo_mapped_relationships 41,911 (100%)
