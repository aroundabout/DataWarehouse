<template>

  <div>

    <el-row :gutter="20">
        <el-col :span="10" :xs="24">
        <el-card>
          <el-row>
                <el-radio v-model="method" label="mysql">mysql</el-radio>
                <el-radio v-model="method" label="hive">hive</el-radio>
                <el-radio v-model="method" label="neo4j">neo4j</el-radio>
            </el-row>
          <br>
          <el-row>
            选择要查询的日期：
          </el-row>
          <br>
          <el-row :gutter="5">
            <el-col :span="10">
            <p>请输入年份</p>
            <el-input-number v-model="yearDate" @change="handleYearChange" :min="1932" :max="2019" label="选择年份"></el-input-number>
            </el-col>
            <el-col :span="10">
            <p>请输入月份</p>
            <el-input-number v-model="monthDate" @change="handleMonthChange" :min="1" :max="12" label="选择月份"></el-input-number>
            </el-col>
            <el-col :span="10">
            <p>请输入日期</p>
            <el-input-number v-model="dayDate" @change="handleDayChange" :min="1" :max="31" label="选择日期"></el-input-number>
            </el-col>
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
        yearDate:1932,
        monthDate:1,
        dayDate:1,
        year:-1,
        month:-1,
        day:-1,
        count:0,
        tableData: [],
        resData: []
    }
  },
  created() {
  },
  methods:{
    handleYearChange(){
      this.year=this.yearDate
    },
    handleMonthChange(){
      this.month=this.monthDate
    },
    handleDayChange(){
      this.day=this.dayDate
    },
    search(){
      console.log(this.method)
      this.tableData=[]
      console.log(this.date)
      if(this.method=="mysql"){
        console.log("search by mysql")
        this.$axios.get("/mysql/getMovie",{
          params: {
            movieName:"defaultText",
            movieType:"defaultText",
            year:this.year,
            month:this.month,
            day:this.day,
            actor:"defaultText",
            director:"defaultText",
            rate:-1,
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
            year:this.year,
            month:this.month,
            day:this.day,
            actor:"defaultText",
            director:"defaultText",
            rate:-1,
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
            year:this.year,
            month:this.month,
            day:this.day,
            actor:"defaultText",
            director:"defaultText",
            rate:-1,
            }
        })
        .then(res=>{
          this.resData = res.data;
          console.log(this.resData.length)
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
      console.log(this.count)
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