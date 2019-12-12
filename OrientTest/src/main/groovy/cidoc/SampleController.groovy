package cidoc

import cidoc.nodeEntities.E1_CRM_Entity
import cidoc.nodeEntities.E55_Type
import com.tinkerpop.blueprints.impls.orient.OrientGraphFactory
import groovy.transform.CompileStatic
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@CompileStatic
class SampleController {

    @Autowired
    OrientGraphFactory graphFactory

    @RequestMapping('/persons')
    def persons() {
        return graphFactory.withTransaction { graph ->
            return personsToJSON(E1_CRM_Entity.graphQuery('select from E1_CRM_Entity'))
        }
    }

    @RequestMapping('/cities')
    def cities() {
        return graphFactory.withTransaction { graph ->
            return personsToJSON(E55_Type.graphQuery('select from E55_Type'))
        }
    }

    static List personsToJSON(def persons) {
        persons.collect { E1_CRM_Entity e1 ->
            [rid          : e1.getP2_has_type().toString()]
        }
    }
}