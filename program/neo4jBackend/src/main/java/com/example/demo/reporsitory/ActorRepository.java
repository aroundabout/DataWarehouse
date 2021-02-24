package com.example.demo.reporsitory;


import com.example.demo.domain.Actor;
import com.example.demo.domain.ActorResult;
import com.example.demo.domain.Product;
import org.neo4j.ogm.model.Result;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.data.neo4j.repository.query.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ActorRepository extends Neo4jRepository<Actor,String> {
    @Query("match (m:Actor)-[r:Director_Actor]-(n:Director) where n.Director=~ $Director return m")
    List<Actor> getActorListByDirector(@Param("Director")String Director);

    @Query("match (m:Actor)-[r:Actor_Actor]-(n:Actor) where m.Actor=~ $Actor return n")
    List<Actor> getActorListByActor(@Param("Actor")String Actor);
}
