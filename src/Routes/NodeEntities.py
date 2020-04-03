from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import \
    E24_Physical_Human_Made_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import \
    E72_Legal_Object

result = E1_CRM_Entity.nodes.get(name="E1 de Teste")
found_e24 = E72_Legal_Object.nodes.get(name="e18_2")

result = E1_CRM_Entity.nodes.get(uid="38fd9e7523ed45808dd9b1219183ebb0")
print(result.to_json())
