from abc import ABC

from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'


class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)


class TerribleCountry(StructuredNode):
    code2 = StringProperty(unique_index=True, required=True)


class BestCountry(Country):
    code3 = StringProperty(unique_index=True, required=True)


class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    country = RelationshipTo(Country, 'IS_FROM')


jim = Person(name='Jim', age=3).save()  # Create
jim.age = 4
jim.save()  # Update, (with validation)
var = jim.id  # neo4j internal id
germany = Country(code='DE').save()
germany2 = TerribleCountry(code2='DE2').save()
superGermany = BestCountry(code='DE', code3='SuperDE').save()
jim.country.connect(germany)
jim.country.connect(superGermany)
