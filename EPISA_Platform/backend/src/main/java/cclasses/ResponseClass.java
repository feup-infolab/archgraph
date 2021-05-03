package cclasses;
import java.util.List;
import java.util.Map;

public class ResponseClass {
    private final Map<String, Object> properties;

    public ResponseClass(Map<String, Object> properties) {
        this.properties = properties;
    }

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
}
