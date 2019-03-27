package cidoc.nodeTraits

import cidoc.nodeEntities.E1_Crm_Entity
import org.neo4j.ogm.annotation.Relationship

trait PC0_CRM_Property_T {

    @Relationship(type="P01_has_domain")
    private E1_Crm_Entity P01_has_domain = new E1_Crm_Entity()

    E1_Crm_Entity getP01(){
        return P01_has_domain
    }

    @Relationship(type="P02_has_range")
    private E1_Crm_Entity P02_has_range = new E1_Crm_Entity()

    E1_Crm_Entity getP02(){
        return P02_has_range
    }

}