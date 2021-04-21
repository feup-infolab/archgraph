package operations;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;

public class FillExamples {
    public String sparqlHost;
    public String dataHost;


        public FillExamples(String sparqlHost, String dataHost) {
            this.sparqlHost = sparqlHost;
            this.dataHost = dataHost;
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
            properties.createProperties();

            // add the property
            res.addProperty(properties.getMaterialProperty(), "papelA3");
            res.addProperty(properties.getMaterialPropertyType(), "papel");

            res.addProperty(properties.getDimensionProperty(), "40m");
            res.addProperty(properties.getDimensionPropertyValue(), "40");
            res.addProperty(properties.getDimensionPropertyMU(), "meter");
            res.addProperty(properties.getDimensionPropertyComponent(), "Component");

            res.addProperty(properties.getQuantityProperty(), "1 Papel");
            res.addProperty(properties.getDimensionPropertyValue(), "1");
            res.addProperty(properties.getDimensionPropertyMU(), "Papel");
            res.addProperty(properties.getQuantityPropertyComponent(), "Component");

            res.addProperty(properties.getConservationProperty(), "Conservado");
            res.addProperty(properties.getConservationIDProperty(), "31/03/1990");
            res.addProperty(properties.getConservationFDProperty(), "01/02/1992");

            res.addProperty(properties.getLanguageProperty(), "Portugues");
            res.addProperty(properties.getLanguageIdentifierProperty(), "PT");

            res.addProperty(properties.getWritingProperty(), "Escrita");
            res.addProperty(properties.getWritingIdentifierProperty(), "1234");

            res.addProperty(properties.getDocProperty(), "Prosa");


            res.addProperty(properties.getTypologyProperty(), "Língua Analítica");

            res.addProperty(properties.getSubjectProperty(), "Assunto do Documento");

            res.addProperty(properties.getAccessConditionProperty(), "Acesso Completo");
            res.addProperty(properties.getAccessConditionJustifificationProperty(), "Disponivel a Todos");

            res.addProperty(properties.getReproductionConditionProperty(), "Ilegal");
            res.addProperty(properties.getReproductionConditionJustifificationProperty(), "Unico");

            res.addProperty(properties.getRelatedEventsProperty(), "1235");
            res.addProperty(properties.getRelatedEventsTypeProperty(), "Teste");
            res.addProperty(properties.getRelatedEventsIDProperty(), "12/06/2000");
            res.addProperty(properties.getRelatedEventsFDProperty(), "12/06/2001");

            res.addProperty(properties.getRelatedDocumentProperty(), res2);
            res.addProperty(properties.getRelatedDocumentProperty(), res3);


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
