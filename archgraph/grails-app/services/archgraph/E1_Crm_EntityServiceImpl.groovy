package archgraph

import cidoc.nodeEntities.E1_Crm_Entity
import grails.gorm.services.Service


@Service(E1_Crm_Entity)
class E1_Crm_EntityServiceImpl extends GenericService<E1_Crm_Entity> implements E1_Crm_EntityService{

    @Override
    Class<E1_Crm_Entity> getEntityType() {
        return E1_Crm_Entity.class
    }
}
