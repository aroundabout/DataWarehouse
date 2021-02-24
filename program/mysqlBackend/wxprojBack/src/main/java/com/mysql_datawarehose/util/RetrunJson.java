package com.mysql_datawarehose.util;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.mysql_datawarehose.constant.ReturnCodeConstant;

public class RetrunJson {
    public static JSONObject returnJsonSuccess(String str){
        JSONObject jsonObject= JSON.parseObject(str);
        JSONObject returnJson=new JSONObject();
        returnJson.put("code", ReturnCodeConstant.OK);
        returnJson.put("msg",ReturnCodeConstant.SUCCESS);
        returnJson.put("data",jsonObject);
        return returnJson;
    }
    public static JSONObject returnJsonArraySuccess(String str){
        JSONArray jsonObject= JSON.parseArray(str);
        JSONObject returnJson=new JSONObject();
        returnJson.put("code", ReturnCodeConstant.OK);
        returnJson.put("msg",ReturnCodeConstant.SUCCESS);
        returnJson.put("data",jsonObject);
        return returnJson;
    }

    public static JSONObject returnJsonFailure(String str){
        JSONObject jsonObject= JSON.parseObject(str);
        JSONObject returnJson=new JSONObject();
        returnJson.put("code", ReturnCodeConstant.ServerError);
        returnJson.put("msg",ReturnCodeConstant.FAILURE);
        returnJson.put("data",jsonObject);
        return returnJson;
    }
}
