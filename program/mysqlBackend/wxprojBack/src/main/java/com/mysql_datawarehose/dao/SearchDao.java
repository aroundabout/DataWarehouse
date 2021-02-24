package com.mysql_datawarehose.dao;


import com.mysql_datawarehose.domain.CooperationInfo;
import com.mysql_datawarehose.domain.Movie_Info;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface SearchDao {

    @Select("SELECT * FROM all_data WHERE ${queryState}")
    List<Movie_Info> queryMovieByInfo(String queryState);

    @Select("select actors as Names from all_data where actors like concat('%',#{actor},'%')")
    List<CooperationInfo> queryActorCooperationByActor(String actor);
    @Select("select actors as Names from all_data where director like concat('%',#{director},'%')")
    List<CooperationInfo> queryActorCooperationByDirector(String director);
    @Select("select director as Names from all_data where actors like concat('%',#{actor},'%')")
    List<CooperationInfo> queryDirectorCooperation(String actor);


}
