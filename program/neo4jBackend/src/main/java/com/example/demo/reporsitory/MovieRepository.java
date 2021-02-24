package com.example.demo.reporsitory;

import com.example.demo.domain.Actor;
import com.example.demo.domain.Product;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.data.neo4j.repository.query.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface MovieRepository extends Neo4jRepository<Product,String> {
    @Query("match (n:Product)-[:Productid_Title]-(m:Title) where m.Title=~ $Title return n ")
    List<Product> getMovieByName(@Param("Title") String Title);

    @Query("match (m:Genre)-[:Title_Genre]-(n:Title)-[:Productid_Title]-(l:Product) where m.Genre=~ $Type return l")
    List<Product> getMovieByType(@Param("Type")String Type);

    @Query("match (m:Director)-[:Title_Director]-(n:Title)-[:Productid_Title]-(k:Product) where m.Director=~ $Director return k ")
    List<Product> getMovieByDirector(@Param("Director")String Director);

    @Query("match (n:Product)-[:Productid_Title]-(:Title)-[:Title_Actor]-(m:Actor) where m.Actor=~ $Actor return n")
    List<Product> getMovieByActor(@Param("Actor")String Actor);


    //注意要改
    @Query("match (p:Product) where p.Rate>=$Rate and p.Rate<$Arate return p")
    List<Product> getMovieByRate(@Param("Rate")double Rate,@Param("Arate")double Arate);


    //时间的查询
    @Query("match (i:Day)-[:ProductId_Day]-(n:Product)-[:ProductId_Yearmonth]-(j:Yearmonth) where i.Day=$Day and j.Yearmonth=$Yearmonth return n")
    List<Product> getMovieYMD(@Param("Day")Integer Day,@Param("Yearmonth")String Yearmonth);

    @Query("match (n:Product)-[:ProductId_Yearmonth]-(m:Yearmonth) where m.Yearmonth=$Yearmonth return n")
    List<Product> getMovieYM(@Param("Yearmonth")String Yearmonth);

    @Query("match (d:Day)-[:ProductId_Day]-(n:Product)-[:ProductId_Year]-(m:Year) where m.Year=$Year and d.Day=$Day return n")
    List<Product> getMovieYD(@Param("Year")Integer Year,@Param("Day")Integer Day);

    @Query("match (n:Product)-[:ProductId_Monthday]-(m:Monthday) where m.Monthday=$Monthday return n")
    List<Product> getMovieMD(@Param("Monthday")String Monthday);

    @Query("match (n:Product)-[:ProductId_Year]-(m:Year) where m.Year=$Year return n ")
    List<Product> getMovieYear(@Param("Year")Integer Year);

    @Query("match (n:Product)-[:ProductId_Month]-(m:Month) where m.Month=$Month return n")
    List<Product> getMovieMonth(@Param("Month")Integer Month);

    @Query("match (n:Product)-[:ProductId_Day]-(m:Day) where m.Day=$Day return n")
    List<Product> getMovieDay(@Param("Day")Integer Day);

}
