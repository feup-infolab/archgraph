package restservice;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

@Configuration
@ConfigurationProperties("config")
public class YAMLConfig {

    private String host;

    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }

    @Profile("dev")
    @Bean
    public void devDataBaseConnection(){
        System.err.println(this.host);
    }

    @Profile("prod")
    @Bean
    public void prodDataBaseConnection(){
        System.err.println(host);
    }

}