package cidoc

import cidoc.nodeEntities.E1_CRM_Entity
import cidoc.nodeEntities.E55_Type
import cidoc.nodeTraits.E55_Type_T
import com.tinkerpop.blueprints.impls.orient.OrientGraph;
import com.tinkerpop.blueprints.impls.orient.OrientGraphFactory;
import groovy.transform.CompileStatic;
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.EnableAutoConfiguration
import org.springframework.boot.builder.SpringApplicationBuilder
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer
import org.springframework.context.ApplicationListener
import org.springframework.context.annotation.Bean
import org.springframework.context.event.ContextRefreshedEvent

@CompileStatic
@EnableAutoConfiguration
class BootApp extends SpringBootServletInitializer implements ApplicationListener<ContextRefreshedEvent> {

    @Autowired
    OrientGraphFactory graphFactory

    /**
     *  Create entities on startup
     * @param event
     */
    @Override
    void onApplicationEvent(ContextRefreshedEvent event) {

            def db = graphFactory.getNoTx().rawGraph
            if(!db.exists()){
                db.create()
            }
            def orient = new OrientGraph(db,false)
            orient.begin()
            def first = new E1_CRM_Entity()
            def second = new E55_Type()
            def third = new E1_CRM_Entity()

            //third.addEdge("e",second.vertexInstance,"P2_has_type_E2")
            orient.addVertex(third,"class",E1_CRM_Entity.class)
          //  orient.addVertex(second)
            //orient.addVertex(third)
            orient.commit()


            def testdb = graphFactory
            def test = graphFactory.findAll()
            def test3 = orient.countEdges()
            def test4 = orient.countVertices()
            def test5 = orient.getVertices().findAll()
             println(test5)
             println(test4)


    }



    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
        application.sources BootApp
    }

    static void main(String[] args) {
        SpringApplication.run BootApp, args
    }

    @Bean
    public OrientGraphFactory databaseFactory() {
        // change to 'remote:host/dbname' if persistent storage needed
        def factory = new OrientGraphFactory("memory:test").setupPool(1, 20)
        factory.autoStartTx = false
        graphFactory = factory
        factory
    }

    @Bean
    SampleController sampleController() {
        new SampleController(graphFactory: graphFactory)
    }

}