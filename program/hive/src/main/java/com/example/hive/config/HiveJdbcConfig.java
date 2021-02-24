package com.example.hive.config;

import org.apache.tomcat.jdbc.pool.DataSource;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;


@Configuration
public class HiveJdbcConfig {

    @Value("${hive.url}")
    private String url;

    @Value("${hive.driver-class-name}")
    private String driver;

    @Value("${hive.user}")
    private String user;


    @Bean
    public DataSource dataSource(){
        DataSource dataSource = new DataSource();
        dataSource.setUrl(url);
        dataSource.setDriverClassName(driver);
        dataSource.setUsername(user);
        //dataSource.setPassword(password);
        return dataSource;
    }

    @Bean
    public JdbcTemplate jdbcTemplate(DataSource dataSource){
        return new JdbcTemplate(dataSource);
    }
}