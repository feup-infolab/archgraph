package operations;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;

import java.util.HashMap;

public  class Resources {
    public Model model;
    public String string200717 = "http://erlangen-crm.org/200717/";
    public String untitledOntology = "http://www.semanticweb.org/dmelo/ontologies/2020/7/untitled-ontology-151#";


    public Resources(Model model) {
        this.model = model;
    }

    public Resource getE42Identifier() {
        return model.getResource(string200717 + "E42_Identifier");
    }

    public Resource getE31Document() {
        return model.getResource(string200717 + "E31_Document");
    }

    public Resource getReferenceCode() {
        return model.getResource(untitledOntology + "Reference_code");
    }

    public Resource getARE5IdentifierType() {
        return model.getResource(untitledOntology + "ARE5_identifierType");
    }

    public Resource getString() {
        return model.getResource("http://www.episa.inesctec.pt/data_object#String");
    }

    public Resource getARE3SuppliedTitle() {
        return model.getResource(untitledOntology + "ARE3SuppliedTitle");
    }

    public Resource getARE2FormalTitle() {
        return model.getResource(untitledOntology + "ARE2FormalTitle");

    }



}