<template>
    <el-container class="home-container">


        <!-- 侧边栏 -->
        <Sidebar/>

        <el-main>
          <!-- 导航栏 -->
          <Navbar/>

          <div v-show="routeName == '首页'" class="home_container">
          </div>    
          <router-view></router-view>
        </el-main>

    </el-container>
</template>

<script>

import Sidebar from "@/components/Sidebar";
import Navbar from "@/components/Navbar";

export default {
  name: "Home",
  computed:{
    routeName(){
        const route = this.$route
        const { meta} = route
        return meta.name
    }
  },
  components:{
    Sidebar,
    Navbar
  },
  data(){
    return{
      // 左侧菜单
      menuList:[],
      
    }
  },

  methods:{
    logout:function(){
      sessionStorage.setItem("isLogin", false);
      sessionStorage.removeItem("userid" );
      //
      location="/login"
    }
  },

}
</script>

<style scoped>

.home-container{
  height: 100%;
}

.el-main {
  padding: 0;
}

.el-header{
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
}

.el-aside{

}

.el-main{
  /* background-color: azure; */
}


</style>
