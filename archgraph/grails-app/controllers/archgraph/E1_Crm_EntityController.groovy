package archgraph

import cidoc.nodeEntities.E1_Crm_Entity

class E1_Crm_EntityController {

    E1_Crm_EntityServiceImpl E1


    static allowedMethods = [save: "POST", update: "PUT", delete: "DELETE"]

    def index() { }

    def show(Long id){
       respond E1.find(id)
    }

    def create(){
        E1_Crm_Entity e1 = new E1_Crm_Entity()
        respond e1
    }




}
