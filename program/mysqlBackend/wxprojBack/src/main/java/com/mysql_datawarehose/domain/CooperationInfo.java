package com.mysql_datawarehose.domain;

import lombok.Builder;
import lombok.Data;
import lombok.ToString;
import lombok.experimental.Tolerate;

import java.io.Serializable;

@ToString
@Builder
@Data
public class CooperationInfo implements Serializable{
    private String Names;
    @Tolerate
    public CooperationInfo(){}
}

