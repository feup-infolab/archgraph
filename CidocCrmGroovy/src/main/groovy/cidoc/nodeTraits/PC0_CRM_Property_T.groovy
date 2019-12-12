package cidoc.nodeTraits

import cidoc.nodeEntities.E1_Crm_Entity
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait PC0_CRM_Property_T {

    @Relationship(type="P01_has_domain")
    private E1_CRM_Entity_T P01_has_domain

    E1_CRM_Entity_T getP01_has_domain(){
        return P01_has_domain
    }

    void setP01_has_domain(E1_CRM_Entity_T e1){
        P01_has_domain = e1

    }

    static Object P01_has_domain_t = E1_CRM_Entity_T.class

    @Relationship(type="P02_has_range")
    private E1_CRM_Entity_T P02_has_range

    E1_CRM_Entity_T getP02_has_range(){
        return P02_has_range
    }

    void setP02_has_range(E1_CRM_Entity_T e1){
        P02_has_range = e1

    }

    static Object P02_has_range_t = E1_CRM_Entity_T.class

}