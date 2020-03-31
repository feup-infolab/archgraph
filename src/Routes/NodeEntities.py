from src.Models.CRM.v5_0_2.NodeEntities.E35_Title import E35_Title
from src.Models.CRM.v5_0_2.NodeEntities.E53_Place import E53_Place
from src.Models.CRM.v5_0_2.NodeEntities.E70_Thing import E70_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E55_Type import E55_Type
from src.Models.CRM.v5_0_2.NodeEntities.E1_CRM_Entity import E1_CRM_Entity
from src.Models.CRM.v5_0_2.NodeEntities.E18_Physical_Thing import E18_Physical_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Human_Made_Thing import E24_Physical_Human_Made_Thing
from src.Models.CRM.v5_0_2.NodeEntities.E52_Time_Span import E52_Time_Span
from src.Models.CRM.v5_0_2.NodeEntities.E72_Legal_Object import E72_Legal_Object
from src.Models.CRM.v5_0_2.NodeEntities.E39_Actor import E39_Actor
from src.Models.CRM.v5_0_2.NodeEntities.E7_Activity import E7_Activity
from src.Models.CRM.v5_0_2.NodeEntities.E21_Person import E21_Person
from src.Models.CRM.v5_0_2.NodeEntities.E2_Temporal_Entity import E2_Temporal_Entity
from src.Models.CRM.v5_0_2.NodeProperties.PC14_Carried_Out_By import PC14_Carried_Out_By


result = E1_CRM_Entity.nodes.get(name="E1 de Teste")
found_e24 = E72_Legal_Object.nodes.get(name="e18_2")

result = E1_CRM_Entity.nodes.get(uid="38fd9e7523ed45808dd9b1219183ebb0")
print(result.to_json())
