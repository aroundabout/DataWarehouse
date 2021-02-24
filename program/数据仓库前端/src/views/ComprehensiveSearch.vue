<template>

  <div>

    <el-row :gutter="20">
        <el-col :span="20" :xs="24">
        <el-card>
            <el-row>
                <el-radio v-model="method" label="mysql">mysql</el-radio>
                <el-radio v-model="method" label="hive">hive</el-radio>
                <el-radio v-model="method" label="neo4j">neo4j</el-radio>
            </el-row>
          <br>
          <el-row>
            输入要查询的电影信息：
          </el-row>
          <br>
          <el-row>
            <el-row :gutter="20">
                <el-col :span="5" :xs="24">
                    <el-input placeholder="请输入电影名称" prefix-icon="el-icon-search" v-model="movieName"></el-input>
                </el-col>
                <el-col :span="5" :xs="24">    
                    <el-input placeholder="请输入演员名字" prefix-icon="el-icon-search" v-model="actor"></el-input>
                </el-col>
                <el-col :span="5" :xs="24">
                    <el-input placeholder="请输入导演名字" prefix-icon="el-icon-search" v-model="director"></el-input>
                </el-col>
                <el-col :span="5" :xs="24">
                    <el-select v-model="movieType" placeholder="请选择电影种类">
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                    </el-select>
                </el-col>
            </el-row>
            <br>
            <el-row>
                <el-radio v-model="radio" label="5">5.0</el-radio>
                <el-radio v-model="radio" label="4">4.0~5.0</el-radio>
                <el-radio v-model="radio" label="3">3.0~4.0</el-radio>
                <el-radio v-model="radio" label="2">2.0~3.0</el-radio>
                <el-radio v-model="radio" label="1">1.0~2.0</el-radio>
                <el-radio v-model="radio" label="0">0.0~1.0</el-radio>
            </el-row>
            <br>
            <!--
            <el-date-picker v-model="date" type="daterange" unlink-panels
                range-separator="至"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
                placeholder="选择日期" value-format="yyyy-MM-dd">
            </el-date-picker>
            -->
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
        options: [{
          value: 'action',
          label: '动作电影'
        }, {
          value: 'adventure',
          label: '冒险电影'
        }, {
          value: 'arthoust',
          label: '艺术电影'
        }, {
          value: 'documentary',
          label: '纪实电影'
        }, {
          value: 'horror',
          label: '恐怖电影'
        }, {
          value: 'special interest',
          label: '特殊爱好电影'
        }, {
          value: 'suspense',
          label: '悬疑电影'
        }, {
          value: 'science fiction',
          label: '科幻电影'
        }, {
          value: 'animation',
          label: '动漫电影'
        }, {
          value: 'kids',
          label: '儿童电影'
        }, {
          value: 'comedy',
          label: '喜剧电影'
        }, {
          value: 'drama',
          label: '戏剧电影'
        }, {
          value: 'war',
          label: '战争电影'
        }, {
          value: 'sports',
          label: '运动电影'
        }],
        yearDate:1932,
        monthDate:1,
        dayDate:1,
        year:-1,
        month:-1,
        day:-1,
        movieName:'',
        movieType:'',
        actor:'',
        director:'',
        radio:'',
        rate:0,
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
      this.tableData=[]
      this.count=0
      if(this.movieName==''){
        this.movieName="defaultText"
      }
      console.log(this.movieType)
      if(this.movieType==''){
        this.movieType="defaultText"
      }
      console.log(this.actor)
      if(this.actor==''){
        this.actor="defaultText"
      }
      console.log(this.director)
      if(this.director==''){
        this.director="defaultText"
      }
      console.log(this.radio)
      if(this.radio==''){
        this.rate=-1
      }
      else{
        this.rate=parseInt(this.radio)
      }
      if(this.method=="mysql"){
        console.log("search by mysql")
        this.$axios.get("/mysql/getMovie",{
          params: {
            movieName: this.movieName,
            movieType:this.movieType,
            year:this.year,
            month:this.month,
            day:this.day,
            actor:this.actor,
            director:this.director,
            rate:this.rate,
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
            movieName: this.movieName,
            movieType:this.movieType,
            year:this.year,
            month:this.month,
            day:this.day,
            actor:this.actor,
            director:this.director,
            rate:this.rate,
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
            movieName: this.movieName,
            movieType:this.movieType,
            year:this.year,
            month:this.month,
            day:this.day,
            actor:this.actor,
            director:this.director,
            rate:this.rate,
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
      this.movieName=null
      this.movieType=null
      this.actor=null
      this.director=null
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