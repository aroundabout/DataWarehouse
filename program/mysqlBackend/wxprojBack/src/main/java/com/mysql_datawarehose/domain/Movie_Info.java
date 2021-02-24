package com.mysql_datawarehose.domain;

import lombok.Builder;
import lombok.Data;
import lombok.ToString;
import lombok.experimental.Tolerate;

import java.io.Serializable;

@ToString
@Builder
@Data
public class Movie_Info implements Serializable {

    private String movieId;
    private String movieName;
    private String director;
    private String actors;
    private String year;
    private String month;
    private String day;
    private String weekday;
    private String version;
    private String movieType;
    private String rate;
    private String reviewNum;
    private String five;
    private String four;
    private String three;
    private String two;
    private String one;

    @Tolerate
    public Movie_Info(){

    }
}
