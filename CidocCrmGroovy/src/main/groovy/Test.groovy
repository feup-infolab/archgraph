import cidoc.Loader
import cidoc.nodeEntities.E1_Crm_Entity
import com.sun.tools.javac.code.Lint

E1_Crm_Entity e1 = new E1_Crm_Entity()
println(e1.p1_is_identified_by_t)

Loader l = new Loader()

//l.getAllRelations("E12_Production")
/*ArrayList<String> s = new ArrayList<>()
s.push("E22_ManMade_Object")
s.push("E1_Crm_Entity")
s.push("E84_E33")
println(l.getCounterDomain("E12_Production","P108_has_produced",s))
*/
l.process()



