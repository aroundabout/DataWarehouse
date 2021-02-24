package com.mysql_datawarehose.service;

import com.mysql_datawarehose.domain.CooperationInfo;
import com.mysql_datawarehose.domain.Movie_Info;

import java.util.List;

public interface SearchService {
//    public List<Movie_Info> getMovieByTitle(String title);
//    public List<Movie_Info> getMovieByTime(String time);
//    public List<Movie_Info> getMovieByDirector(String director);
//    public List<Movie_Info> getMovieByActor(String actor);
//    public List<Movie_Info> getMovieByTag(String tag);
//    public List<Movie_Info> getMovieByRate(String rate);
    public List<Movie_Info> getMovieByInfo(String movieName,
                                           String actor,
                                           String director,
                                           String movieType,
                                           String year,
                                           String month,
                                           String day,
                                           int rate);

    public List<CooperationInfo> getActorCooperationInfoByActor(String actor);
    public List<CooperationInfo> getActorCooperationInfoByDirector(String director);
    public List<CooperationInfo> getDirectorCooperationInfo(String actor);

}
