package operations;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;

public class FillExamples {
    public String sparqlHost;
    public String dataHost;
    public String updateHost;


        public FillExamples(String defaultHost) {
            this.sparqlHost = defaultHost + "sparql";
            this.dataHost = defaultHost + "data";
            this.updateHost = defaultHost + "update";
        }

        public void fill() {
            RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                    .destination(dataHost);


        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Model model = conn.fetch();

            // create the resource
            Resource res = model.getResource("http://erlangen-c<    rm.org/200717/E31_Document1");
            Resource res2 = model.getResource("http://erlangen-crm.org/200717/E31_Document113");
            Resource res3 = model.getResource("http://erlangen-crm.org/200717/E31_Document127");

            Properties properties= new Properties(model);

            // add the property
            res.addProperty(properties.getHasMaterial(), "papelA3");
            res.addProperty(properties.getHasMaterialType(), "papel");

            res.addProperty(properties.getDimension(), "40m");
            res.addProperty(properties.getHasDimensionValue(), "40");
            res.addProperty(properties.getHasDimensionMU(), "meter");
            res.addProperty(properties.getHasDimensionComponent(), "Component");

            res.addProperty(properties.getHasQuantity(), "1 Papel");
            res.addProperty(properties.getHasDimensionValue(), "1");
            res.addProperty(properties.getHasDimensionMU(), "Papel");
            res.addProperty(properties.getHasQuantityComponent(), "Component");

            res.addProperty(properties.getHasConservationStatus(), "Conservado");
            res.addProperty(properties.getHasConservationStatusID(), "31/03/1990");
            res.addProperty(properties.getHasConservationStatusFD(), "01/02/1992");

            res.addProperty(properties.getHasLanguage(), "Portugues");
            res.addProperty(properties.getHasLanguageIdentifier(), "PT");

            res.addProperty(properties.getHasWriting(), "Escrita");
            res.addProperty(properties.getHasWritingIdentifier(), "1234");

            res.addProperty(properties.getHasDocTradition(), "Prosa");


            res.addProperty(properties.getHasTypology(), "Língua Analítica");

            res.addProperty(properties.getHasSubject(), "Assunto do Documento");

            res.addProperty(properties.getHasAccessCondition(), "Acesso Completo");
            res.addProperty(properties.getHasAccessConditionJustifification(), "Disponivel a Todos");

            res.addProperty(properties.getHasReproductionCondition(), "Ilegal");
            res.addProperty(properties.getReproductionConditionJustifificationProperty(), "Unico");

            res.addProperty(properties.getHasRelatedEvents(), "1235");
            res.addProperty(properties.getHasRelatedEventsType(), "Teste");
            res.addProperty(properties.getHasRelatedEventsID(), "12/06/2000");
            res.addProperty(properties.getHasRelatedEventsFD(), "12/06/2001");

            res.addProperty(properties.getHasRelatedDocument(), res2);
            res.addProperty(properties.getHasRelatedDocument(), res3);


            conn.put(model);
            conn.commit();
        }
    }
//
//
//    public static void main(String args[]) {
//
//    }
}
