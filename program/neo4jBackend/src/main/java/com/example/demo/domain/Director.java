package com.example.demo.domain;


import lombok.Data;
import org.neo4j.ogm.annotation.NodeEntity;
import org.springframework.data.annotation.Id;

@Data
@NodeEntity(label = "Director")
public class Director {
    @Id
    private String Directorid;
    private String Director;
    @Override
    public boolean equals(Object arg) {
        Director a=(Director)arg;
        return Directorid.equals(a.Directorid)&& Director.equals(a.Director);
    }

    @Override
    public int hashCode() {
        return this.Directorid.hashCode();
    }
}
