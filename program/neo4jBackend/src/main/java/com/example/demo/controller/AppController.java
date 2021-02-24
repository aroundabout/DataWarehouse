package com.example.demo.controller;


import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.example.demo.domain.Actor;
import com.example.demo.domain.ActorResult;
import com.example.demo.domain.Director;
import com.example.demo.domain.Product;
import com.example.demo.reporsitory.ActorRepository;
import com.example.demo.reporsitory.DirectorRepository;
import com.example.demo.reporsitory.MovieRepository;
import org.neo4j.ogm.model.Result;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.config.annotation.InterceptorRegistration;

import javax.annotation.Resource;
import javax.swing.*;
import java.util.*;

@RestController
@RequestMapping("/neo4j")
public class AppController {
    @Resource
    private MovieRepository movieRepository;
    @Resource
    private ActorRepository actorRepository;
    @Resource
    private DirectorRepository directorRepository;

    @RequestMapping(value = "/getRelationByDirector", method = RequestMethod.GET)
    public JSONArray getRelationByDirector(
            @RequestParam("directorName") String directorName
    ) {
        List<Actor> list = actorRepository.getActorListByDirector(".*"+directorName+".*");
        Map<String, Integer> dict = new HashMap<>();
        for (Actor actor : list) {
            String id = actor.getActorid();
            String name = actor.getActor();
            if (dict.containsKey(name)) {
                Integer temp = dict.get(name);
                temp += 1;
                dict.put(name, temp);
            } else {
                dict.put(name, 1);
            }
        }
        JSONArray jsonArray = new JSONArray();
        for (Map.Entry<String, Integer> entry : dict.entrySet()) {
            JSONObject jsonObject = new JSONObject();
            jsonObject.put("actorName", entry.getKey());
            jsonObject.put("times", entry.getValue());
            jsonArray.add(jsonObject);
        }
        return jsonArray;
    }

    @RequestMapping(value = "/cooperation",method =RequestMethod.GET)
    public JSONArray getActorByActor(
            @RequestParam("actorName") String actorName
    ) {
        List<Actor> list = actorRepository.getActorListByActor(".*"+actorName+".*");
        Map<String, Integer> dict = new HashMap<>();
        for (Actor actor : list) {
            String id = actor.getActorid();
            String name = actor.getActor();
            if (dict.containsKey(name)) {
                Integer temp = dict.get(name);
                temp += 1;
                dict.put(name, temp);
            } else {
                dict.put(name, 1);
            }
        }
        JSONArray jsonArray = new JSONArray();
        for (Map.Entry<String, Integer> entry : dict.entrySet()) {
            JSONObject jsonObject = new JSONObject();
            jsonObject.put("actorName", entry.getKey());
            jsonObject.put("times", entry.getValue());
            jsonArray.add(jsonObject);
        }
        return jsonArray;
    }
    @RequestMapping(value = "/getRelationByActor",method = RequestMethod.GET)
    public JSONArray getDirectorByActor(
            @RequestParam("actorName") String actorName
    ){
        List<Director> list =directorRepository.getDirectorByActor(".*"+actorName+".*");
        Map<String, Integer> dict = new HashMap<>();
        for (Director director : list) {
            String name = director.getDirector();
            if (dict.containsKey(name)) {
                Integer temp = dict.get(name);
                temp += 1;
                dict.put(name, temp);
            } else {
                dict.put(name, 1);
            }
        }
        JSONArray jsonArray = new JSONArray();
        for (Map.Entry<String, Integer> entry : dict.entrySet()) {
            JSONObject jsonObject = new JSONObject();
            jsonObject.put("directorName", entry.getKey());
            jsonObject.put("times", entry.getValue());
            jsonArray.add(jsonObject);
        }
        return jsonArray;
    }



    @RequestMapping(value = "/getMovie", method = RequestMethod.GET)
    public JSONArray getMovie(
            @RequestParam("movieName") String movieName,
            @RequestParam("movieType") String movieType,
            @RequestParam("year") Integer year,
            @RequestParam("month") Integer month,
            @RequestParam("day") Integer day,
            @RequestParam("actor") String actor,
            @RequestParam("director") String director,
            @RequestParam("rate") Double rate
    ) {
        Set<Product> productSet = new HashSet<>();
        List<Product> listName = new ArrayList<>();
        List<Product> listType = new ArrayList<>();
        List<Product> listDate = new ArrayList<>();
        List<Product> listActor = new ArrayList<>();
        List<Product> listDirector = new ArrayList<>();
        List<Product> listRate = new ArrayList<>();
        if (!movieName.equals("defaultText")) {
            listName = movieRepository.getMovieByName(".*"+movieName+".*");
            productSet.addAll(listName);
        }
        if (!movieType.equals("defaultText")) {
            listType = movieRepository.getMovieByType(".*"+movieType+".*");
            if (productSet.size() == 0) {
                productSet.addAll(listType);
            } else {
                Set<Product> tempset = new HashSet<>();
                productSet.retainAll(tempset);
                if (productSet.size() == 0) {
                    String jsonStr = JSONObject.toJSONString(productSet);
                    return JSON.parseArray(jsonStr);
                }
            }
        }
        if (!actor.equals("defaultText")) {
            listActor = movieRepository.getMovieByActor(".*"+actor+".*");
            if (productSet.size() == 0) {
                productSet.addAll(listActor);
            } else {
                Set<Product> tempset = new HashSet<>(listActor);
                productSet.retainAll(tempset);
                if (productSet.size() == 0) {
                    String jsonStr = JSONObject.toJSONString(productSet);
                    return JSON.parseArray(jsonStr);
                }
            }
        }
        if (!director.equals("defaultText")) {
            listDirector = movieRepository.getMovieByDirector(".*"+director+".*");
            if (productSet.size() == 0) {
                productSet.addAll(listDirector);
            } else {
                Set<Product> tempset = new HashSet<>(listDirector);
                productSet.retainAll(tempset);
                if (productSet.size() == 0) {
                    String jsonStr = JSONObject.toJSONString(productSet);
                    return JSON.parseArray(jsonStr);
                }
            }
        }
        if (rate != -1) {
            double arate=rate+1;
            listRate = movieRepository.getMovieByRate(rate,arate);
            if (productSet.size() == 0) {
                productSet.addAll(listRate);
            } else {
                Set<Product> tempset = new HashSet<>(listRate);
                productSet.retainAll(tempset);
                if (productSet.size() == 0) {
                    String jsonStr = JSONObject.toJSONString(productSet);
                    return JSON.parseArray(jsonStr);
                }
            }
        }

        if (!(year==-1) && !(month==-1) && !(day==-1)) {
            String ym = year + "." + month;
            listDate = movieRepository.getMovieYMD(day, ym);
        } else if (!(year==-1) && !(month==-1)) {
            String ym = year + "." + month;
            listDate = movieRepository.getMovieYM(ym);
        } else if (!(year==-1) && !(day==-1)) {
            listDate = movieRepository.getMovieYD(year, day);
        } else if (!(month==-1) && !(day==-1)) {
            String md = month + "." + day;
            listDate = movieRepository.getMovieMD(md);
        } else if (!(year==-1)) {
            listDate = movieRepository.getMovieYear(year);
        } else if (!(month==-1)) {
            listDate = movieRepository.getMovieMonth(month);
        } else if (!(day==-1)) {
            listDate = movieRepository.getMovieDay(day);
        }

        if (productSet.size() == 0) {
            productSet.addAll(listDate);
        } else {
            if(!(year==-1&& month==-1&& day==-1 )){
                Set<Product> tempset = new HashSet<>(listDate);
                productSet.retainAll(tempset);
                if (productSet.size() == 0) {
                    String jsonStr = JSONObject.toJSONString(productSet);
                    return JSON.parseArray(jsonStr);
                }
            }

        }
        String jsonStr = JSONObject.toJSONString(productSet);
        return JSON.parseArray(jsonStr);
    }

}
