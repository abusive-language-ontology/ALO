# Cross-Resource Query Evaluation

This directory contains the SPARQL queries and results used to evaluate
cross-resource retrieval in the ALO knowledge graph.

The evaluation examines whether the semantic links established during
knowledge graph construction support queries across the resource-specific
named graphs. The queries represent selected integration scenarios rather
than an exhaustive evaluation of all possible cross-resource queries.

The evaluated scenarios include:

- retrieval of SALD abusive text spans through their NIF representations
  and links to AloLex lexical entries;
- retrieval of synthetic dataset entries together with the corresponding
  AloLex lexical entries, lexical senses, canonical forms, and definitions;
- retrieval of SALD occurrences and synthetic examples associated with
  the same AloLex lexical entry; and
- retrieval of AloLex lexical senses together with original lexicographic
  usage examples and synthetically generated examples.

Each query directory contains the SPARQL query files and the corresponding
query results used in the evaluation reported in the accompanying paper.

These scenarios demonstrate cross-resource retrieval through the explicit
semantic links established among SALD, NIF representations, AloLex, and the
synthetic dataset. They are intended to assess the queryability of the
integrated resources and should not be interpreted as a general benchmark
of semantic interoperability.
