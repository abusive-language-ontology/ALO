\## ALO Vocabulary Conformance Validation



The generated RDF resources were checked for conformance with the

ALO vocabulary before their integration into the knowledge graph.



The validation verifies:



\- whether all ALO terms referenced in a target RDF resource are

&#x20; defined in the ALO ontology;

\- whether ALO terms used as predicates are declared as properties;

\- whether ALO terms used as objects of `rdf:type` are declared as

&#x20; classes;

\- whether ALO classes are incorrectly used as predicates;

\- whether ALO properties are incorrectly used as objects.



The script also reports missing `rdfs:label` and `rdfs:comment`

annotations for ALO classes and properties.



The validation was performed separately for the AloLex, SALD,

and synthetic-data RDF resources.



No undefined or structurally inconsistent ALO references were

identified in the validated resources.

