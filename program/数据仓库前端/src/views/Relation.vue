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
            <el-radio v-model="radio" label="actor">演员</el-radio>
            <el-radio v-model="radio" label="director">导演</el-radio>
          </el-row>
          <br>
          <el-row>
            输入人名：
          </el-row>
          <br>
          <el-row>
            <el-input placeholder="请输入名字" prefix-icon="el-icon-search" v-model="value">
            </el-input>
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
                prop="actorName"
                label="演员名字">
            </el-table-column>
            <el-table-column
                prop="directorName"
                label="导演名称">
            </el-table-column>
            <el-table-column
                prop="times"
                label="合作次数">
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
        value:"",
        radio:"",
        count:0,
        tableData: [],
        resData: []
    }
  },
  created() {
  },
  methods:{
  compare(property){
      return function(a,b){
        var value1 = a[property];
        var value2 = b[property];
        return value2-value1;
    }
  },
    search(){
      console.log(this.method)
      this.tableData=[]
      this.count=0
      console.log(this.radio)
      console.log(this.value)
      if(this.value.length>0){
        if(this.method=="mysql"){
        console.log("search by mysql")
        if(this.radio=="actor"){
        this.$axios.get("/mysql/getRelationByActor",{
          params: {
            actorName:this.value,
            }
        })
        .then(res=>{
          this.resData = res.data.data;
          console.log(this.resData)
          for(var i=0;i<res.data.data.length;i++){
            var temp={};
            temp.actorName=this.value;
            temp.directorName=this.resData[i]["directorName"];
            temp.times=this.resData[i]["times"];
            this.tableData.push(temp);
            this.count=res.data.data.length;
          }
        })
        .catch(err=>{
        console.log(err);
        })
        }
        if(this.radio=="director"){
        this.$axios.get("/mysql/getRelationByDirector",{
          params: {
            directorName:this.value,
            }
        })
        .then(res=>{
          this.resData = res.data.data;
          console.log(this.resData)
          for(var i=0;i<res.data.data.length;i++){
            var temp={};
            temp.actorName=this.resData[i]["actorName"];
            temp.directorName=this.value;
            temp.times=this.resData[i]["times"];
            this.tableData.push(temp);
            this.count=res.data.data.length;
          }
        })
        .catch(err=>{
        console.log(err);
        })
        }
      }
      if(this.method=="hive"){
        console.log("search by hive")
        if(this.radio=="actor"){
        this.$axios.get("/hive/getRelationByActor",{
          params: {
            actorName:this.value,
            }
        })
        .then(res=>{
          this.resData = res.data;
          console.log(this.resData)
          for(var i=0;i<res.data.length;i++){
            var temp={};
            temp.actorName=this.value;
            temp.directorName=this.resData[i]["directorName"];
            temp.times=this.resData[i]["times"];
            this.tableData.push(temp);
            this.count=res.data.length;
          }
        })
        .catch(err=>{
        console.log(err);
        })
        }
        if(this.radio=="director"){
        this.$axios.get("/hive/getRelationByDirector",{
          params: {
            directorName:this.value,
            }
        })
        .then(res=>{
          this.resData = res.data;
          console.log(this.resData)
          for(var i=0;i<res.data.length;i++){
            var temp={};
            temp.actorName=this.resData[i]["actorName"];
            temp.directorName=this.value;
            temp.times=this.resData[i]["times"];
            this.tableData.push(temp);
            this.count=res.data.length;
          }
          this.tableData.sort(this.compare("times"))
        })
        .catch(err=>{
        console.log(err);
        })
        }
      }
      if(this.method=="neo4j"){
        console.log("search by neo4j")
        if(this.radio=="actor"){
        this.$axios.get("/neo4j/getRelationByActor",{
          params: {
            actorName:this.value,
            }
        })
        .then(res=>{
          this.resData = res.data;
          console.log(this.resData)
          for(var i=0;i<res.data.length;i++){
            var temp={};
            temp.actorName=this.value;
            temp.directorName=this.resData[i]["directorName"];
            temp.times=this.resData[i]["times"];
            this.tableData.push(temp);
            this.count=res.data.length;
          }
          this.tableData.sort(this.compare("times"))
        })
        .catch(err=>{
        console.log(err);
        })
        }
        if(this.radio=="director"){
        this.$axios.get("/neo4j/getRelationByDirector",{
          params: {
            directorName:this.value,
            }
        })
        .then(res=>{
          this.resData = res.data;
          console.log(this.resData)
          for(var i=0;i<res.data.length;i++){
            var temp={};
            temp.actorName=this.resData[i]["actorName"];
            temp.directorName=this.value;
            temp.times=this.resData[i]["times"];
            this.tableData.push(temp);
            this.count=res.data.length;
          }
          this.tableData.sort(this.compare("times"))
        })
        .catch(err=>{
        console.log(err);
        })
        }
      }
      }
      else{
        alert("请输入人名")
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