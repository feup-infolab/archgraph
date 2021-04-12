package restservice;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

@Configuration
@ConfigurationProperties("config")
public class YAMLConfig {

    private String sparqlHost;
    private String dataHost;

    public String getSparqlHost() {
        return sparqlHost;
    }

    public String getDataHost() {
        return dataHost;
    }


    public void setSparqlHost(String sparqlHost) {
        this.sparqlHost = sparqlHost;
    }

    public void setDataHost(String dataHost) {
        this.dataHost = dataHost;
    }


    @Profile("dev")
    @Bean
    public void devDataBaseConnection() {
        System.out.println("my sparqlHost:" + this.sparqlHost);
        System.out.println("my dataHost:" + this.dataHost);
    }

    @Profile("prod")
    @Bean
    public void prodDataBaseConnection() {
        System.out.println("my sparqlHost:" + this.sparqlHost);
        System.out.println("my dataHost:" + this.dataHost);
    }
}