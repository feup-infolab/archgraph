package cidoc.nodeTraits

import Xsd_String
import groovy.transform.CompileStatic
import lombok.Getter
import lombok.Setter


@CompileStatic
@Getter
@Setter
trait E18_Physical_Thing_T implements E72_Legal_Object_T, E92_Spacetime_Volume_T{
    ArrayList<E57_Material_T> P45_consists_of = new ArrayList<>()
    ArrayList<E18_Physical_Thing_T> P46_is_composed_of = new ArrayList<>()
    Xsd_String AP11_has_materials
}