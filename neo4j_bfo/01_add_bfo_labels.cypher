// ==========================================
// ISGO v3.0 - Add BFO Labels to Nodes
// ISO/IEC 21838-2 Compliance - Step 1
// ==========================================

// Step 1: Label NISTControl nodes
MATCH (n:NISTControl)
SET n:Continuant, n:InformationContentEntity
RETURN count(n) as nist_controls_labeled;
// Expected: 1,196 nodes

// Step 2: Label AIRMFRequirement nodes
MATCH (n:AIRMFRequirement)
SET n:Continuant, n:InformationContentEntity
RETURN count(n) as airm_requirements_labeled;
// Expected: 19 nodes

// Step 3: Label MITRETechnique nodes
MATCH (n:MITRETechnique)
SET n:Occurrent, n:Process
RETURN count(n) as mitre_techniques_labeled;
// Expected: 356 nodes

// Step 4: Label Asset nodes (if exist)
MATCH (n:Asset)
SET n:IndependentContinuant
RETURN count(n) as assets_labeled;

// Step 5: Label System nodes (if exist)
MATCH (n:System)
SET n:IndependentContinuant
RETURN count(n) as systems_labeled;

// Next: Run 02_add_bfo_relationship_properties.cypher
