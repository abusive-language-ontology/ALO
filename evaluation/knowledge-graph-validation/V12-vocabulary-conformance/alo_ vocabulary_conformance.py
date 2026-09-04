from rdflib import Graph, Namespace
from rdflib.namespace import RDF, OWL, RDFS

# =====================
# CONFIG
# =====================

ALO_ONTOLOGY_FILE = "alo_13072026.ttl" # name of alo ontology file
TARGET_FILE = "synthetic_kg_alolex_20260902.ttl"   # name of validated file: sald.ttl, synthetic.ttl...
TARGET_FORMAT = "turtle"     # turtle, xml, nt...

ALO = Namespace("http://llod.jerteh.rs/alo/alo.owl#")

# =====================
# LOAD GRAPHS
# =====================

alo_g = Graph()
alo_g.parse(ALO_ONTOLOGY_FILE, format="turtle")   # if alo file has extension *.owl then format = RDF/XML

target_g = Graph()
target_g.parse(TARGET_FILE, format=TARGET_FORMAT)

# =====================
# TERMS DEFINED IN ALO
# =====================

defined_classes = set()
defined_properties = set()
defined_individuals = set()

for s in alo_g.subjects(RDF.type, OWL.Class):
    if str(s).startswith(str(ALO)):
        defined_classes.add(s)

for s in alo_g.subjects(RDF.type, RDFS.Class):
    if str(s).startswith(str(ALO)):
        defined_classes.add(s)

for prop_type in [
    OWL.ObjectProperty,
    OWL.DatatypeProperty,
    OWL.AnnotationProperty,
    RDF.Property,
]:
    for p in alo_g.subjects(RDF.type, prop_type):
        if str(p).startswith(str(ALO)):
            defined_properties.add(p)

for s in alo_g.subjects(RDF.type, OWL.NamedIndividual):
    if str(s).startswith(str(ALO)):
        defined_individuals.add(s)

defined_terms = defined_classes | defined_properties | defined_individuals

# =====================
# TERMS USED IN TARGET
# =====================

used_alo_terms = set()
used_alo_predicates = set()
used_alo_classes_or_individuals = set()

for s, p, o in target_g:
    if str(s).startswith(str(ALO)):
        used_alo_terms.add(s)

    if str(p).startswith(str(ALO)):
        used_alo_terms.add(p)
        used_alo_predicates.add(p)

    if str(o).startswith(str(ALO)):
        used_alo_terms.add(o)
        used_alo_classes_or_individuals.add(o)

# =====================
# CHECKS
# =====================

missing_terms = sorted(used_alo_terms - defined_terms, key=str)
missing_properties = sorted(used_alo_predicates - defined_properties, key=str)

# class used in rdf:type but not defined as class
undefined_classes = set()

for s, p, o in target_g.triples((None, RDF.type, None)):
    if str(o).startswith(str(ALO)) and o not in defined_classes:
        undefined_classes.add(o)

undefined_classes = sorted(undefined_classes, key=str)

# ALO terms used as predicate but defined as class
class_used_as_property = sorted(
    [p for p in used_alo_predicates if p in defined_classes],
    key=str
)

# ALO terms used as object but defined as property
property_used_as_object = sorted(
    [o for o in used_alo_classes_or_individuals if o in defined_properties],
    key=str
)

# =====================
# LABEL / COMMENT CHECK FOR ALO ONTOLOGY
# =====================

missing_labels = []
missing_comments = []

for term in sorted(defined_classes | defined_properties, key=str):
    if not list(alo_g.objects(term, RDFS.label)):
        missing_labels.append(term)
    if not list(alo_g.objects(term, RDFS.comment)):
        missing_comments.append(term)

# =====================
# REPORT
# =====================

print("====================================")
print("ALO GRAPH VALIDATION REPORT")
print("====================================")
print(f"Ontology file: {ALO_ONTOLOGY_FILE}")
print(f"Target file:   {TARGET_FILE}")
print("------------------------------------")

print(f"Defined ALO classes:      {len(defined_classes)}")
print(f"Defined ALO properties:   {len(defined_properties)}")
print(f"Defined ALO individuals:  {len(defined_individuals)}")
print(f"Used ALO terms in target: {len(used_alo_terms)}")

print("------------------------------------")
print(f"Missing ALO terms:        {len(missing_terms)}")
for t in missing_terms:
    print("  ", t)

print("------------------------------------")
print(f"Missing ALO properties:   {len(missing_properties)}")
for t in missing_properties:
    print("  ", t)

print("------------------------------------")
print(f"Undefined ALO classes in rdf:type: {len(undefined_classes)}")
for t in undefined_classes:
    print("  ", t)

print("------------------------------------")
print(f"Class used as property: {len(class_used_as_property)}")
for t in class_used_as_property:
    print("  ", t)

print("------------------------------------")
print(f"Property used as object: {len(property_used_as_object)}")
for t in property_used_as_object:
    print("  ", t)

print("------------------------------------")
print(f"ALO classes/properties without rdfs:label: {len(missing_labels)}")
for t in missing_labels[:30]:
    print("  ", t)

print("------------------------------------")
print(f"ALO classes/properties without rdfs:comment: {len(missing_comments)}")
for t in missing_comments[:30]:
    print("  ", t)

print("====================================")
print("Done.")

