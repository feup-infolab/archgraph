package archgraph

import grails.gorm.services.Service

@Service(CidocEntity)
interface CidocEntityService {

    CidocEntity get(Serializable id)

    List<CidocEntity> list(Map args)

    Long count()

    void delete(Serializable id)

    CidocEntity save(CidocEntity cidocEntity)

}