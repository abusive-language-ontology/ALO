# Knowledge Graph Validation

This directory contains the validation queries and results used to assess
the structural and referential integrity of the ALO knowledge graph and
its conformance with the ALO ontology vocabulary.

The validation focuses on the instantiated RDF data across the
resource-specific named graphs and checks whether the representations and
semantic links introduced during knowledge graph construction are
structurally consistent.

The validation includes checks for:

- completeness of SALD entry representation;
- presence of the expected `AbusivenessSet` instances associated with
  abusive language analyses;
- completeness and consistency of NIF span representations, including
  reference contexts, anchors, and character offsets;
- validity of NIF character offsets;
- referential integrity of links from SALD abusive spans to AloLex lexical
  entries;
- consistency between ALO and ITS RDF lexical-entry references;
- referential integrity of lexical-entry and lexical-sense links from the
  synthetic dataset to AloLex; and
- conformance of the generated RDF resources with the ALO ontology
  vocabulary.

## ALO Vocabulary Conformance

The generated RDF resources were checked for conformance with the ALO
ontology vocabulary. The checks verify that:

- all referenced ALO terms are defined in the ontology;
- predicates from the ALO namespace correspond to declared properties;
- ALO terms used as objects of `rdf:type` statements are declared as
  classes; and
- ALO classes and properties are not used in incompatible RDF positions.

The initial conformance checks identified discrepancies between the
generated RDF resources and the ALO ontology vocabulary. These discrepancies
were reviewed and corrected during knowledge graph refinement. The validation
was subsequently repeated on the final version of the knowledge graph.

The final validation completed successfully, with no undefined ALO terms,
undeclared ALO predicates, or structurally inconsistent uses of ALO classes
and properties identified.