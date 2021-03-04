package cclasses;

import java.util.List;
import java.util.Map;

public class ResponseClass {

    //private final String id;

    //private final String $schema;

    //private final String description;

    //private final String type;

    private final Map<String, Object> properties;


    public ResponseClass(Map<String, Object> properties) {
        //this.id = "https://example.com/arrays.schema.json";
        this.properties = properties;


    }

    //public String getId() {
    //    return id;
    //}

    public Map<String, Object> getProperties() {
        return properties;
    }

    public void putProperties(String key, Object ob) {
        this.properties.put(key, ob);
    }


    public void addContent(String key, Map<String, String> value) {
        properties.put(key, value);
    }

    public void addList(String key, List<Map<String, String>> value) {
        properties.put(key, value);
    }

    /*public String get$schema() {
        return $schema;
    }

    public String getDescription() {
        return description;
    }

    public String getType() {
        return type;
    }*/
}
