package archgraph

import cidoc.Loader
import org.neo4j.ogm.session.Session

class HomeController {

    E1_Crm_EntityServiceImpl E1 = new E1_Crm_EntityServiceImpl()


    def index() {

        respond([name: session.name ?: 'User', entityTotal: E1.getCount()])
    }

    def updateName(String name) {
        session.name = name

        flash.message = "Name has been updated"

        redirect action: 'index'
    }
}
