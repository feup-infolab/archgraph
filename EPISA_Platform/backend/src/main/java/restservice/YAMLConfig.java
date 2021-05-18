package restservice;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

@Configuration
@ConfigurationProperties("config")
public class YAMLConfig {

    private String myHost;

    public String getMyHost() {
        return myHost;
    }

    public void setMyHost(String myHost) {
        this.myHost = myHost;
    }

    @Profile("dev")
    @Bean
    public void devDataBaseConnection() {
        System.out.println("my myHost:" + this.myHost);
    }

    @Profile("prod")
    @Bean
    public void prodDataBaseConnection() {
        System.out.println("my myHost:" + this.myHost);
    }
}