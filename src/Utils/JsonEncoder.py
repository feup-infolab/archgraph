from json import JSONEncoder
from neomodel import db


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def json_merge(json_a, json_b):
    json_a = json_a[:-1] + "," + json_b[1:]

    return json_a


def index_creation():
    result_index = db.cypher_query("CALL db.index.fulltext.createNodeIndex('node_entity',['E1_CRM_Entity', "
                                   "'E2_Temporal_Entity' , 'E3_Condition_State' , 'E4_Period' , 'E5_Event' , "
                                   "'E6_Destruction' , 'E7_Activity' , 'E8_Acquisition' , 'E9_Move' , "
                                   "'E10_Transfer_of_Custody' , 'E11_Modification' , 'E12_Production' , "
                                   "'E13_Attribute_Assignment' , 'E14_Condition_Assessment' , "
                                   "'E15_Identifier_Assignment' , 'E16_Measurement' , 'E17_Type_Assignment' , "
                                   "'E18_Physical_Thing' , 'E19_Physical_Object' , 'E20_Biological_Object' , "
                                   "'E21_Person' , 'E22_Human_Made_Object' , 'E24_Physical_Human_Made_Thing' , "
                                   "'E25_Human_Made_Feature' , 'E26_Physical_Feature' , 'E27_Site' , "
                                   "'E28_Conceptual_Object' , 'E29_Design_or_Procedure' , 'E30_Right' , "
                                   "'E31_Document' , 'E32_Authority_Document' , 'E33_Linguistic_Object' , "
                                   "'E34_Inscription' , 'E35_Title' , 'E36_Visual_Item' , 'E37_Mark' , 'E39_Actor' , "
                                   "'E41_Appellation' , 'E42_Identifier' , 'E52_Time_Span' , 'E53_Place' , "
                                   "'E54_Dimension' , 'E55_Type' , 'E56_Language' , 'E57_Material' , "
                                   "'E58_Measurement_Unit' , 'E63_Beggining_of_Existence' , 'E64_End_of_Existence' , "
                                   "'E65_Creation' , 'E66_Formation' , 'E67_Birth' , 'E68_Dissolution' , 'E69_Death' "
                                   ", 'E70_Thing' , 'E71_Human_Made_Thing' ,'E72_Legal_Object', "
                                   "'E73_Information_Object' , 'E74_Group' , 'E77_Persistent_Item' , "
                                   "'E78_Curated_Holding' , 'E79_Part_Addition' , 'E80_Part_Removal' , "
                                   "'E81_Transformation' , 'E83_Type_Creation' , 'E85_Joining' , 'E86_Leaving' , "
                                   "'E87_Curation_Activity' , 'E89_Propositional_Object' ,'E90_Symbolic_Object', "
                                   "'E92_Spacetime_Volume' , 'E93_Presence' , 'E96_Purchase' , 'E97_Monetary_Amount' "
                                   ", 'E98_Currency' , 'E99_Product_Type'],['name'])")


class cidoc_search_results:
    def __init__(self, label, property):
        self.labels = label
        self.properties = property


def search_cidoc(name):
    results, meta = db.cypher_query("CALL db.index.fulltext.queryNodes('node_entity','" + name + "~')")
    results_list = []

    for i in range(len(results)):
        result = cidoc_search_results(results[i][0]._labels, results[i][0]._properties)
        results_list.append(result)

    return results_list
