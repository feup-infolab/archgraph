package cidoc.nodeTraits

import cidoc.nodeEntities.Xsd_String
import groovy.transform.CompileStatic
import org.neo4j.ogm.annotation.Relationship

@CompileStatic
trait E18_Physical_Thing_T implements E72_Legal_Object_T, E92_Spacetime_Volume_T{

    @Relationship(type="P45_consists_of")
    ArrayList<E57_Material_T> P45_consists_of = new ArrayList<>()

    ArrayList<E57_Material_T> getP45_consists_of(){
        return P45_consists_of
    }

    static Object P45_consists_of_t = E57_Material_T.class


    @Relationship(type="P46_is_composed_of")
    ArrayList<E18_Physical_Thing_T> P46_is_composed_of = new ArrayList<>()

    ArrayList<E18_Physical_Thing_T> getP46_is_composed_of(){
        return P46_is_composed_of
    }

    static Object P46_is_composed_of_t = E18_Physical_Thing_T.class


    @Relationship(type="AP11_has_materials")
    Xsd_String AP11_has_materials

    Xsd_String AP11_has_materialsAP11(){
        return AP11_has_materials
    }

    void setAP11_has_materials(Xsd_String ap11){
        AP11_has_materials = ap11
    }

}