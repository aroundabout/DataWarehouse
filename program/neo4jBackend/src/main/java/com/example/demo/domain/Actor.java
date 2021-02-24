package com.example.demo.domain;

import lombok.Data;
import org.neo4j.ogm.annotation.NodeEntity;
import org.springframework.data.annotation.Id;

@Data
@NodeEntity(label = "Actor")
public class Actor {
    @Id
    private String Actorid;
    private String Actor;
    @Override
    public boolean equals(Object arg) {
        Actor a=(Actor)arg;
        return Actorid.equals(a.Actorid)&& Actor.equals(a.Actor);
    }

    @Override
    public int hashCode() {
        return this.Actorid.hashCode();
    }
}
