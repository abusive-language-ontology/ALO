# ALO: Abusive Language Ontology

ALO (Abusive Language Ontology) is a domain ontology for the semantic
representation of abusive language concepts, annotations, analyses, and
related linguistic resources. It serves as the semantic core of an
ontology-centered knowledge graph framework for integrating heterogeneous
abusive language resources while preserving their resource-specific
representations.

The framework combines ALO with established Semantic Web vocabularies and
standards, including PROV-O, OntoLex-Lemon, the NLP Interchange Format (NIF),
ITS RDF, LexInfo, Lexicog, DCTerms, and SKOS.

## Repository Structure

This repository contains the ALO ontology, its documentation, and the
artefacts supporting the evaluation reported in the accompanying research
paper.

- `ontology/` — the authoritative ALO ontology file.
- `evaluation/ontology-validation/` — ontology validation artefacts,
  including HermiT and OOPS! evaluation results.
- `evaluation/knowledge-graph-validation/` — SPARQL queries and results used
  to assess the structural and referential integrity of the instantiated
  knowledge graph and its conformance with the ALO ontology vocabulary.
- `evaluation/cross-resource-query-evaluation/` — representative
  cross-resource SPARQL queries and their corresponding results.
- `docs/` — WIDOCO-generated human-readable ontology documentation used for
  the GitHub Pages deployment.

## Ontology Documentation

Human-readable documentation of the ALO ontology is generated using WIDOCO
and is available at:

https://abusive-language-ontology.github.io/ALO/

The authoritative ontology source is maintained in the `ontology/`
directory. The files in `docs/` contain the generated documentation.

## Knowledge Graph

The ALO framework has been instantiated as a knowledge graph integrating
ALO, the AloLex abusive language lexicon, the SALD manually annotated
abusive language corpus, NIF-based representations of abusive text spans,
and a synthetic abusive language dataset.

The resulting knowledge graph comprises 506,338 RDF triples organized
across four resource-specific named graphs.

To avoid unrestricted redistribution of the underlying social media
content, the instantiated knowledge graph is not distributed as a public
RDF dump. Controlled access to the knowledge graph may be provided for
research and evaluation purposes.

## Evaluation

The repository provides the artefacts supporting the three evaluation
components reported in the accompanying paper:

1. ontology validation;
2. knowledge graph validation; and
3. cross-resource query evaluation.

The evaluation materials include ontology validation reports, SPARQL
validation queries, cross-resource queries, and their corresponding results.

## License

ALO is licensed under the Creative Commons Attribution 4.0 International
(CC BY 4.0) license.

See the `LICENSE` file for details.

## Citation

If you use ALO or the associated resources in your research, please cite
the accompanying publication.

Citation metadata are provided in `CITATION.cff`.

The full bibliographic reference will be added after publication of the
accompanying paper.

© 2026 Danka Jokic


