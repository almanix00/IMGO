// ==========================================
// ISGO v3.0 - Add BFO Relationship Properties
// ISO/IEC 21838-2 Compliance - Step 2
// ==========================================

// Step 1: MITIGATES → realized_in
MATCH ()-[r:MITIGATES]->()
SET r.bfo_type = "realized_in"
RETURN count(r) as mitigates_updated;
// Expected: 20,658 relationships

// Step 2: ADDRESSES/RELATED_TO/BELONGS_TO → is_about
MATCH ()-[r:ADDRESSES]->()
SET r.bfo_type = "is_about"
WITH count(r) as addresses_count
MATCH ()-[r:RELATED_TO]->()
SET r.bfo_type = "is_about"
WITH addresses_count, count(r) as related_count
MATCH ()-[r:BELONGS_TO]->()
SET r.bfo_type = "is_about"
RETURN addresses_count, related_count, count(r) as belongs_count;
// Expected total: 21,219 relationships

// Step 3: USES → participates_in
MATCH ()-[r:USES]->()
SET r.bfo_type = "participates_in"
RETURN count(r) as uses_updated;
// Expected: 34 relationships

// Next: Run 03_verify_bfo_integration.cypher
