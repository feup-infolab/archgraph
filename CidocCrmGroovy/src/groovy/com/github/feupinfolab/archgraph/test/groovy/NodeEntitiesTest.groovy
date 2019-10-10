
/*
import cidoc.nodeEntities.E1_CRM_Entity
import cidoc.nodeEntities.E40_Legal_Body
import cidoc.nodeEntities.E41_Appellation
import cidoc.nodeEntities.E55_Type
import cidoc.nodeEntities.E7_Activity
import cidoc.nodeEntities.Entity
import cidoc.nodeTraits.E55_Type_T
import org.junit.Before
import org.junit.Rule

import spock.lang.Shared
import spock.lang.Specification
import spock.lang.Unroll
import org.junit.Test


class NodeEntitiesTest {



    @Rule
    @Delegate(interfaces = false)
    // public Neo4jRule neoServer = new Neo4jRule()

    // private Session session

    @Before
   void setup() throws Exception{
     // Configuration configuration = new Configuration.Builder().uri(neoServer.boltURI().toString()).build()
        //SessionFactory sessionFactory = new SessionFactory(configuration, "cidoc.nodeEntities")
        // session = sessionFactory.openSession()
        // session.purgeDatabase()


    }

    @Test
    void entityTest(){
        E1_CRM_Entity e1 = new E1_CRM_Entity()
        session.save(e1)

        Collection<E1_CRM_Entity> allEntities = session.loadAll(E1_CRM_Entity)
        assert allEntities.size()==1

        session.purgeDatabase()

    }

    @Test
    void relationshipTest() {
        E1_CRM_Entity e1 = new E1_CRM_Entity()
        E41_Appellation e41 = new E41_Appellation()
        e1.p1.add(e41)
        session.save(e1)
        session.save(e41)

        Collection<Entity> entities= session.loadAll(Entity)

        assert entities.size() == 2

        Collection<E1_CRM_Entity> e1s = session.loadAll(E1_CRM_Entity)
        ArrayList<E1_CRM_Entity> first = (E1_CRM_Entity[]) e1s.toArray()
        assert first.get(0).p1.get(0) == e41

        session.purgeDatabase()

    }




    GraphDatabaseService dummy

    def setup(){
        dummy = graphDatabaseService
    }

    def "availability"(){
        expect:
        graphDatabaseService != null

    }

    def "by default a feature method has no transactional context"() {
        when: "trigger a write operation"
        graphDatabaseService.createNode()

        then:
        thrown(NotInTransactionException)
    }

    
    def "withNeo4jTransaction provides transactional"() {

        expect: "empty database"
        Iterables.count(graphDatabaseService.allNodes) == 0

        when:
        graphDatabaseService.createNode()

        then:
        notThrown NotInTransactionException
        Iterables.count(graphDatabaseService.allNodes) == 1
    }

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

}*/
