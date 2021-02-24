package com.example.hive.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/hive")
public class HiveController {

    @Autowired
    @Qualifier("jdbcTemplate")
    private JdbcTemplate jdbcTemplate;

    @RequestMapping("/check")
    public List<Map<String, Object>> list() {
        String sql = "show tables";
        List<Map<String, Object>> list = jdbcTemplate.queryForList(sql);
        return list;
    }
    @RequestMapping("/getMovie")
    public List<Map<String, Object>> getMovie(String movieName,String movieType,int year,int month,int day,String actor,String director,int rate) {
        String sql = String.format("select id,title from movie where " +
                "('%s'='defaultText' or title='%s') and" +
                "('%s'='defaultText' or locate('%s',tags)>0) and" +
                "('%s'='defaultText' or locate('%s',actors)>0) and" +
                "('%s'='defaultText' or locate('%s',directors)>0) and" +
                "(%d=-1 or (rate>=%d and rate<%d+1)) and" +
                "(%d=-1 or year=%d) and" +
                "(%d=-1 or month=%d) and" +
                "(%d=-1 or day=%d)",
                movieName,movieName,
                movieType,movieType,
                actor,actor,
                director,director,
                rate,rate,rate,
                year,year,
                month,month,
                day,day);
        List<Map<String, Object>> list = jdbcTemplate.queryForList(sql);
        return list;
    }

    @RequestMapping("/cooperation")
    public List<Map<String, Object>> getCoActor(String actorName)
    {
        String sql=String.format("select actors from movie where " +
                "locate('%s',actors)>0"
                ,actorName);
        List<Map<String,Object>> list=jdbcTemplate.queryForList(sql);
        Map<String,Integer> count = new HashMap<>();
        for(Map<String,Object>l:list)
        {
            String actors= (String) l.get("actors");
            actors= (String) actors.subSequence(1,actors.length()-1);
            String[] actorList = actors.split(",");
            for(int i=0;i<actorList.length;i++)
            {
                String actor=actorList[i];
                if(!actor.equals(actorName))
                {
                    if(!count.containsKey(actor))
                    {
                        count.put(actor,1);
                    }
                    else
                    {
                        count.put(actor,count.get(actor)+1);
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
        return mapList;
    }

    @RequestMapping("/getRelationByActor")
    public List<Map<String, Object>> getRelationByActor(String actorName)
    {
        String sql=String.format("select directors from movie where " +
                        "locate('%s',actors)>0"
                ,actorName);
        List<Map<String,Object>> list=jdbcTemplate.queryForList(sql);
        Map<String,Integer> count = new HashMap<>();
        for(Map<String,Object>l:list)
        {
            String directors= (String) l.get("directors");
            directors= (String) directors.subSequence(1,directors.length()-1);
            String[] directorList = directors.split(",");
            for(int i=0;i<directorList.length;i++)
            {
                String director=directorList[i];

                    if(!count.containsKey(director))
                    {
                        count.put(director,1);
                    }
                    else
                    {
                        count.put(director,count.get(director)+1);
                    }

            }
        }
        List<Map<String,Object>> mapList= new LinkedList<>();
        for(String key:count.keySet())
        {
            Map<String,Object> map=new HashMap<>();
            map.put("directorName",key);
            map.put("times",count.get(key));
            mapList.add(map);
        }
        return mapList;
    }

    @RequestMapping("/getRelationByDirector")
    public List<Map<String, Object>> getRelationByDirector(String directorName)
    {
        String sql=String.format("select actors from movie where " +
                        "locate('%s',directors)>0"
                ,directorName);
        List<Map<String,Object>> list=jdbcTemplate.queryForList(sql);
        Map<String,Integer> count = new HashMap<>();
        for(Map<String,Object>l:list)
        {
            String actors= (String) l.get("actors");
            actors= (String) actors.subSequence(1,actors.length()-1);
            String[] actorList = actors.split(",");
            for(int i=0;i<actorList.length;i++)
            {
                String actor=actorList[i];

                    if(!count.containsKey(actor))
                    {
                        count.put(actor,1);
                    }
                    else
                    {
                        count.put(actor,count.get(actor)+1);
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
        return mapList;
    }
}