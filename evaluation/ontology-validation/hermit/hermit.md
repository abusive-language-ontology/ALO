# HermiT Reasoner Validation

The logical consistency of ALO was evaluated using the HermiT
reasoner (v1.4.3.456) integrated in Protégé 5.6.5.

The ontology was classified by precomputing the class hierarchy,
object and data property hierarchies, class and property assertions,
and same-individual inferences. The reasoning process completed
successfully, with no logical inconsistencies or unsatisfiable
named classes detected.

- `hermit_log.txt` contains the Protégé reasoner log.
- `hermit_classification.png` shows the inferred class hierarchy
  after classification.