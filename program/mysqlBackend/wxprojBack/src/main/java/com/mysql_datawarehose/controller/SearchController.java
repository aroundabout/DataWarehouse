package com.mysql_datawarehose.controller;


import com.alibaba.fastjson.JSONObject;
import com.mysql_datawarehose.domain.CooperationInfo;
import com.mysql_datawarehose.domain.Movie_Info;
import com.mysql_datawarehose.service.SearchService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.*;


@RestController
@RequestMapping("/mysql")
public class SearchController {

    @Autowired
    private SearchService searchService;

    @RequestMapping(value="/getMovie",method = RequestMethod.GET)
    public JSONObject getMovie(
            @RequestParam("movieName") String movieName,
            @RequestParam("actor") String actor,
            @RequestParam("director") String director,
            @RequestParam("movieType") String movieType,
            @RequestParam("year") String year,
            @RequestParam("month") String month,
            @RequestParam("day") String day,
            @RequestParam("rate") int rate
            ){
         List<Movie_Info> movie_infos=searchService.getMovieByInfo(movieName,actor,director,movieType,year,month,day,rate);
         JSONObject returnjson=new JSONObject();
         returnjson.put("data",movie_infos);
         return returnjson;
    }

    @RequestMapping(value="/getRelationByDirector",method = RequestMethod.GET)
    public JSONObject getRelationByDirector(@RequestParam("directorName") String director)
    {
        List<CooperationInfo> cooperationInfos=searchService.getActorCooperationInfoByDirector(director);
        Map<String,Integer> count=new HashMap<String,Integer>();
        for (CooperationInfo item:cooperationInfos) {
            String names=item.getNames();
            String[] nameList=names.split(",");
            for (String name : nameList)
            {
                if(!name.equals(director))
                {
                    if(!count.containsKey(name))
                    {
                        count.put(name,1);
                    }
                    else
                    {
                        count.put(name,count.get(name)+1);
                    }
                }
            }
        }
        List<Map<String,Object>> mapList= new LinkedList<>();
        for(String key:count.keySet())
        {
            Map<String,Object> map=new HashMap<>();
            map.put("actorName",key);
            map.put("times",count.get(key));
            mapList.add(map);
        }
        JSONObject returnjson=new JSONObject();
        returnjson.put("data",mapList);
        return returnjson;
    }

    @RequestMapping(value="/getRelationByActor",method = RequestMethod.GET)
    public JSONObject getRelationByActor(@RequestParam("actorName") String actor)
    {
        List<CooperationInfo> cooperationInfos=searchService.getDirectorCooperationInfo(actor);
        Map<String,Integer> count=new HashMap<String,Integer>();
        for (CooperationInfo item:cooperationInfos) {
            String names=item.getNames();
            String[] nameList=names.split(",");
            for (String name : nameList)
            {
                if(!name.equals(actor))
                {
                    if(!count.containsKey(name))
                    {
                        count.put(name,1);
                    }
                    else
                    {
                        count.put(name,count.get(name)+1);
                    }
                }
            }
        }
        List<Map<String,Object>> mapList= new LinkedList<>();
        for(String key:count.keySet())
        {
            Map<String,Object> map=new HashMap<>();
            map.put("actorName",key);
            map.put("times",count.get(key));
            mapList.add(map);
        }
        JSONObject returnjson=new JSONObject();
        returnjson.put("data",mapList);
        return returnjson;
    }

    @RequestMapping(value="/cooperation",method = RequestMethod.GET)
    public JSONObject getRelation(@RequestParam("actorName") String actor)
    {
        List<CooperationInfo> cooperationInfos=searchService.getActorCooperationInfoByActor(actor);
        Map<String,Integer> count=new HashMap<String,Integer>();
        for (CooperationInfo item:cooperationInfos) {
            String names=item.getNames();
            String[] nameList=names.split(",");
            for (String name : nameList)
            {
                if(!name.equals(actor))
                {
                    if(!count.containsKey(name))
                    {
                        count.put(name,1);
                    }
                    else
                    {
                        count.put(name,count.get(name)+1);
                    }
                }
            }
        }
        List<Map<String,Object>> mapList= new LinkedList<>();
        for(String key:count.keySet())
        {
            Map<String,Object> map=new HashMap<>();
            map.put("actorName",key);
            map.put("times",count.get(key));
            mapList.add(map);
        }
        JSONObject returnjson=new JSONObject();
        returnjson.put("data",mapList);
        return returnjson;
    }

}
