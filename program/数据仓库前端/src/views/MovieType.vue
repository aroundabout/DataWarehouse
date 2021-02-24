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
            选择查询的电影种类：
          </el-row>
          <br>
          <el-row>
            <el-select v-model="value" placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
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
        value: '',
        count:0,
        tableData: [],
        resData: []
    }
  },
  created() {
  },
  methods:{
    search(){
      console.log(this.method)
      this.tableData=[]
      console.log(this.value)
      if(this.value.length>0){
              if(this.method=="mysql"){
        console.log("search by mysql")
        this.$axios.get("/mysql/getMovie",{
          params: {
            movieName:"defaultText",
            movieType:this.value,
            year:-1,
            month:-1,
            day:-1,
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
            movieType:this.value,
            year:-1,
            month:-1,
            day:-1,
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
            movieType:this.value,
            year:-1,
            month:-1,
            day:-1,
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
        alert("请选择电影类型")
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