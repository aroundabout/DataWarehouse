<template>

  <div>

    <el-row :gutter="20">
        <el-col :span="12" :xs="24">
        <el-card>
          <el-row>
                <el-radio v-model="method" label="mysql">mysql</el-radio>
                <el-radio v-model="method" label="hive">hive</el-radio>
                <el-radio v-model="method" label="neo4j">neo4j</el-radio>
            </el-row>
          <br>
          <el-row>
            <el-radio v-model="radio" label="5">5.0</el-radio>
            <el-radio v-model="radio" label="4">4.0~5.0</el-radio>
            <el-radio v-model="radio" label="3">3.0~4.0</el-radio>
            <el-radio v-model="radio" label="2">2.0~3.0</el-radio>
            <el-radio v-model="radio" label="1">1.0~2.0</el-radio>
            <el-radio v-model="radio" label="0">1.0~2.0</el-radio>
          </el-row>
          <br>
          <el-button icon="el-icon-search" circle type="info" @click="search"></el-button>
          <p>共计{{count}}条查询结果</p>
        </el-card>
        </el-col>
        </el-row>

      <el-row>
            <el-table
                :data="tableData"
                stripe
                style="width: 100%">
            <el-table-column
                prop="movieId"
                label="电影id">
            </el-table-column>
            <el-table-column
                prop="movieName"
                label="电影名称">
            </el-table-column>
            </el-table>
      </el-row>
  </div>
</template>

<script>
export default {
  data(){
    return{
      method:'',
        radio:"",
        count:0,
        tableData: [],
        resData: []
    }
  },
  created() {
  },
  methods:{
    search(){
      this.tableData=[]
      this.count=0
      console.log(this.method)
      console.log(this.radio)
      if(this.radio.length>0){
        if(this.method=="mysql"){
        console.log("search by mysql")
        this.$axios.get("/mysql/getMovie",{
          params: {
            movieName:"defaultText",
            movieType:"defaultText",
            year:-1,
            month:-1,
            day:-1,
            actor:"defaultText",
            director:"defaultText",
            rate:parseInt(this.radio),
            }
        })
        .then(res=>{
          this.resData = res.data.data;
          console.log(this.resData.data)
          for(var i=0;i<res.data.data.length;i++){
            var temp={};
            temp.movieId=this.resData[i]["movieId"];
            temp.movieName=this.resData[i]["movieName"];
            this.tableData.push(temp);
            this.count=res.data.data.length;
          }
        })
        .catch(err=>{
        console.log(err);
        })
      }
      if(this.method=="hive"){
        console.log("search by hive")
        this.$axios.get("/hive/getMovie",{
          params: {
            movieName:"defaultText",
            movieType:"defaultText",
            year:-1,
            month:-1,
            day:-1,
            actor:"defaultText",
            director:"defaultText",
            rate:parseInt(this.radio),
            }
        })
        .then(res=>{
          this.resData = res.data;
          console.log(this.resData)
          for(var i=0;i<res.data.length;i++){
            var temp={};
            temp.movieId=this.resData[i]["id"];
            temp.movieName=this.resData[i]["title"];
            this.tableData.push(temp);
            this.count=res.data.length;
          }
        })
        .catch(err=>{
        console.log(err);
        })
      }
      if(this.method=="neo4j"){
        console.log("search by neo4j")
        this.$axios.get("/neo4j/getMovie",{
          params: {
            movieName:"defaultText",
            movieType:"defaultText",
            year:-1,
            month:-1,
            day:-1,
            actor:"defaultText",
            director:"defaultText",
            rate:parseInt(this.radio),
            }
        })
        .then(res=>{
          this.resData = res.data;
          console.log(this.resData)
          for(var i=0;i<res.data.length;i++){
            var temp={};
            temp.movieId=this.resData[i]["productId"];
            temp.movieName=this.resData[i]["title"];
            this.tableData.push(temp);
            this.count=res.data.length;
          }
        })
        .catch(err=>{
        console.log(err);
        })
      }
      }
      else{
        alert("请选择评分范围")
      }
    }
  }
}
</script>

<style scoped>

.stockcost_container {
  margin-top: 10px;
  margin-left: 10px;
  margin-right: 10px;
}

</style>