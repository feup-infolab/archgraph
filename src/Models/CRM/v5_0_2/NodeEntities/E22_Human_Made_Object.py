from src.Models.CRM.v5_0_2.NodeEntities.E20_Biological_Object import (
    E20_Biological_Object,
)
from src.Models.CRM.v5_0_2.NodeEntities.E19_Physical_Object import E19_Physical_Object
from src.Models.CRM.v5_0_2.NodeEntities.E24_Physical_Man_Made_Thing import (
    E24_Physical_Man_Made_Thing,
)


class E22_Human_Made_Object(E19_Physical_Object, E24_Physical_Man_Made_Thing):
    pass
