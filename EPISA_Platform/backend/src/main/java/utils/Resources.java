package utils;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;

import java.util.HashMap;

public class Resources {
    public Model model;
    public String string200717 = "http://erlangen-crm.org/200717/";
    public String untitledOntology = "http://www.episa.inesctec.pt/archonto/registo1-15#";
    public String stringOwl = "http://www.w3.org/2002/07/owl#";


    public Resources() {
        this.model = ModelFactory.createDefaultModel();
    }



    public Resource getE31Document() {
        return model.getResource(string200717 + "E31_Document");
    }

    public Resource getReferenceCode() {
        return model.getResource(untitledOntology + "referenceCode");
    }

    public Resource getARE5IdentifierType() {
        return model.getResource(untitledOntology + "ARE5_identifierType");
    }

    public Resource getARE1LevelofDescription() {
        return model.getResource(untitledOntology + "ARE1LevelofDescription");
    }


    public Resource getNamedIndividual() {
        return model.getResource(stringOwl + "NamedIndividual");
    }
}