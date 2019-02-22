import cidoc.nodeEntities.E1_Crm_Entity
import cidoc.nodeEntities.E41_Appellation
import spock.lang.Shared
import spock.lang.Specification
import spock.lang.Unroll

@Unroll
class NodeEntitiesTest extends Specification{

    @Shared E1_Crm_Entity e1 = new E1_Crm_Entity()
    @Shared E41_Appellation e41 = new E41_Appellation()

    def "E1 creation"(){
        expect:

        e1.getId() == null
        e1.p1.isEmpty()


    }

    def "E1 name"(){
        when:
        e1.setName("E1 Entity")

        then:
        e1.getName()=="E1 Entity"

    }

    def "P1 Relationship creation"(){
        when:
        e1.p1.add(e41)

        then:
        e1.p1.size() == 1
        e1.p1.get(0) == e41

    }
}
