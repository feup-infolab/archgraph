package showcase;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdfconnection.RDFConnectionFuseki;
import org.apache.jena.rdfconnection.RDFConnectionRemoteBuilder;

public class FillExamples {

    public static void main(String args[]) {
        RDFConnectionRemoteBuilder builder = RDFConnectionFuseki.create()
                .destination("http://localhost:3030/name/data");
        //.destination("http://localhost:3030/name/sparql");


        try (RDFConnectionFuseki conn = (RDFConnectionFuseki) builder.build()) {
            Model model = conn.fetch();

            // create the resource
            Resource res = model.getResource("http://erlangen-crm.org/200717/E31_Document1");
            Resource res2 = model.getResource("http://erlangen-crm.org/200717/E31_Document113");
            Resource res3 = model.getResource("http://erlangen-crm.org/200717/E31_Document127");
            Property materialProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_material");
            Property materialPropertyType = model.createProperty("http://erlangen-crm.org/200717/", "has_material_type");

            Property dimensionProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension");
            Property dimensionPropertyValue = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension_value");
            Property dimensionPropertyMU = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension_measurement_unit");
            Property dimensionPropertyComponent = model.createProperty("http://erlangen-crm.org/200717/", "has_dimension_component");


            Property quantityProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity");
            Property quantityPropertyValue = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity_value");
            Property quantityPropertyMU = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity_measurement_unit");
            Property quantityPropertyComponent = model.createProperty("http://erlangen-crm.org/200717/", "has_quantity_component");


            Property conservationProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_conservation_status");
            Property conservationIDProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_conservation_status_ID");
            Property conservationFDProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_conservation_status_FD");


            Property languageProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_language");
            Property languageIdentifierProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_language_identifier");

            Property writingProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_writing");
            Property writingPropertyIdentifier = model.createProperty("http://erlangen-crm.org/200717/", "has_writing_identifier");

            Property docProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_doc_tradition");

            Property typologyProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_typology");

            Property subjectProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_subject");

            Property accessConditionProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_access_condition");
            Property accessConditionJustifificationProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_access_condition_justification");

            Property reproductionConditionProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_reproduction_condition");
            Property reproductionConditionJustifificationProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_reproduction_condition_justification");


            Property relatedEventsProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_related_event");
            Property relatedEventsTypeProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_related_event_type");
            Property relatedEventsIDProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_related_event_id");
            Property relatedEventsFDProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_related_event_fd");


            Property relatedDocumentProperty = model.createProperty("http://erlangen-crm.org/200717/", "has_related_document");


            // add the property
            res.addProperty(materialProperty, "papelA3");
            res.addProperty(materialPropertyType, "papel");

            res.addProperty(dimensionProperty, "40m");
            res.addProperty(dimensionPropertyValue, "40");
            res.addProperty(dimensionPropertyMU, "meter");
            res.addProperty(dimensionPropertyComponent, "Component");

            res.addProperty(quantityProperty, "1 Papel");
            res.addProperty(quantityPropertyValue, "1");
            res.addProperty(quantityPropertyMU, "Papel");
            res.addProperty(quantityPropertyComponent, "Component");

            res.addProperty(conservationProperty, "Conservado");
            res.addProperty(conservationIDProperty, "31/03/1990");
            res.addProperty(conservationFDProperty, "01/02/1992");

            res.addProperty(languageProperty, "Portugues");
            res.addProperty(languageIdentifierProperty, "PT");

            res.addProperty(writingProperty, "Escrita");
            res.addProperty(writingPropertyIdentifier, "1234");

            res.addProperty(docProperty, "Prosa");


            res.addProperty(typologyProperty, "Língua Analítica");

            res.addProperty(subjectProperty, "Assunto do Documento");

            res.addProperty(accessConditionProperty, "Acesso Completo");
            res.addProperty(accessConditionJustifificationProperty, "Disponivel a Todos");

            res.addProperty(reproductionConditionProperty, "Ilegal");
            res.addProperty(reproductionConditionJustifificationProperty, "Unico");

            res.addProperty(relatedEventsProperty, "1235");
            res.addProperty(relatedEventsTypeProperty, "Teste");
            res.addProperty(relatedEventsIDProperty, "12/06/2000");
            res.addProperty(relatedEventsFDProperty, "12/06/2001");

            res.addProperty(relatedDocumentProperty, res2);
            res.addProperty(relatedDocumentProperty, res3);


            conn.put(model);
            conn.commit();
        }
    }
}
