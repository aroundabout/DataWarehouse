package com.example.demo.reporsitory;

import com.example.demo.domain.Actor;
import com.example.demo.domain.Director;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.data.neo4j.repository.query.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface DirectorRepository  extends Neo4jRepository<Director,String> {
    @Query("match (m:Actor)-[r:Director_Actor]-(n:Director) where m.Actor=~ $Actor return n")
    List<Director> getDirectorByActor(@Param("Actor")String Actor);

}
