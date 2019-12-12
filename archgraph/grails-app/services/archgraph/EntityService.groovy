package archgraph

import grails.gorm.services.Service

@Service(Entity)
interface EntityService {

    Entity get(Serializable id)

    List<Entity> list(Map args)

    Long count()

    void delete(Serializable id)

    Entity save(Entity entity)

}