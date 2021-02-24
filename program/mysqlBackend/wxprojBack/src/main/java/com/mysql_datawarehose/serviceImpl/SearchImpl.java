package com.mysql_datawarehose.serviceImpl;

import com.mysql_datawarehose.dao.SearchDao;
import com.mysql_datawarehose.domain.CooperationInfo;
import com.mysql_datawarehose.domain.Movie_Info;
import com.mysql_datawarehose.service.SearchService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service("SearchService")
public class SearchImpl implements SearchService{

    @Autowired
    private SearchDao searchDao;

    @Override
    public List<Movie_Info> getMovieByInfo(String movieName,
                                           String actor,
                                           String director,
                                           String movieType,
                                           String year,
                                           String month,
                                           String day,
                                           int rate){

        String queryState= "";
        int lowerRate,upperRate;
        if (rate!=-1)
        {
            lowerRate=rate;
            upperRate=rate+1;
            queryState+="all_data.rate BETWEEN "+ lowerRate +" AND "+upperRate;
        }


        if(!movieName.equals("defaultText"))
        {
            if(queryState.equals("")){
                queryState+="all_data.movieName LIKE concat('%','"+movieName+"','%')";
            }
            else{
            queryState+=" AND "+"all_data.movieName LIKE concat('%','"+movieName+"','%')";
            }
        }

        if(!actor.equals("defaultText"))
        {
            if(queryState.equals("")){
                queryState+="all_data.actors LIKE concat('%','"+actor+"','%')";
            }
            else{
                queryState+=" AND "+"all_data.actors LIKE concat('%','"+actor+"','%')";
            }
        }
        if(!director.equals("defaultText"))
        {
            if(queryState.equals("")){
                queryState+="all_data.director LIKE concat('%','"+director+"','%')";
            }
            else{
                queryState+=" AND "+"all_data.director LIKE concat('%','"+director+"','%')";
            }
        }
        if(!movieType.equals("defaultText"))
        {
            if(queryState.equals("")){
                queryState+="all_data.movieType LIKE concat('%','"+movieType+"','%')";
            }
            else{
                queryState+=" AND "+"all_data.movieType LIKE concat('%','"+movieType+"','%')";
            }
        }
        if(!year.equals("-1"))
        {
            if(queryState.equals("")){
                queryState+="all_data.year = "+year;
            }
            else{
                queryState+=" AND "+"all_data.year = "+year;
            }
        }
        if(!month.equals("-1"))
        {
            if(queryState.equals("")){
                queryState+="all_data.month = "+month;
            }
            else{
                queryState+=" AND "+"all_data.month = "+month;
            }
        }
        if(!day.equals("-1"))
        {
            if(queryState.equals("")){
                queryState+="all_data.day = "+day;
            }
            else{
                queryState+=" AND "+"all_data.day = "+day;
            }
        }
        System.out.println(queryState);
        return searchDao.queryMovieByInfo(queryState);

    };
    @Override
    public List<CooperationInfo> getActorCooperationInfoByActor(String actor){
        return searchDao.queryActorCooperationByActor(actor);
    }
    @Override
    public List<CooperationInfo> getActorCooperationInfoByDirector(String director){
        return searchDao.queryActorCooperationByDirector(director);
    }
    @Override
    public List<CooperationInfo> getDirectorCooperationInfo(String actor){
        return searchDao.queryDirectorCooperation(actor);
    }


//    @Override
//    public List<Movie_Info> getMovieByTitle(String title){
//        return searchDao.getUserByTitle(title);
//    };
//    @Override
//    public List<Movie_Info> getMovieByTime(String time){};
//    @Override
//    public List<Movie_Info> getMovieByDirector(String director){};
//    @Override
//    public List<Movie_Info> getMovieByActor(String actor){};
//    @Override
//    public List<Movie_Info> getMovieByTag(String tag){};

}
