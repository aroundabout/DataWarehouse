<template>

    <div class="navbar">

      <i class="el-icon-s-operation" id="switch" @click="setCollapse"></i>
      
      <p>{{routeName}}</p>

      <div class="navbar-item-blank-center"></div>
    </div>

</template>

<script>
export default {
  name: 'Navbar',
  computed:{
    routeName(){
        const route = this.$route
        const { meta} = route
        return meta.name
    }
  },
  data () {
    return {

    }
  },
  methods:{
    setCollapse(){
      this.$store.state.sideBarCollapse = !this.$store.state.sideBarCollapse;
    },
    // 退出登录逻辑
    logout:function(){
      sessionStorage.setItem("isLogin", false);
      sessionStorage.removeItem("userid" );
      location="/login"

    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src="../assets/css/navbar.css"></style>