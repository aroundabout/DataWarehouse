<template>

  <el-aside class="sidebar">

    <el-menu router :default-active="activeIndex" :collapse="this.$store.state.sideBarCollapse">

      <el-menu-item index="/">
        <i class="el-icon-menu"></i>
        <a slot="title">首页</a>
      </el-menu-item>

      <el-menu-item index="/chart">
        <i class="el-icon-upload"></i>
        <a slot="title">执行时间</a>
      </el-menu-item>

      <el-submenu index="/" class="submenu">
        <template slot="title">
            <i class="el-icon-search"></i>
            <a slot="title">查询</a>
        </template>
        <el-menu-item index="/timeSearch">
            <i class="el-icon-search"></i>
            <a slot="title">按照时间查询</a>
        </el-menu-item>
        <el-menu-item index="/movieNameSearch">
            <i class="el-icon-search"></i>
            <a slot="title">按照电影名查询</a>
        </el-menu-item>
        <el-menu-item index="/movieTypeSearch">
            <i class="el-icon-search"></i>
            <a slot="title">按照电影类别查询</a>
        </el-menu-item>
        <el-menu-item index="/directorSearch">
            <i class="el-icon-search"></i>
            <a slot="title">按照导演查询</a>
        </el-menu-item>
        <el-menu-item index="/actorSearch">
            <i class="el-icon-search"></i>
            <a slot="title">按照演员查询</a>
        </el-menu-item>
        <el-menu-item index="/relationSearch">
            <i class="el-icon-search"></i>
            <a slot="title">按照演员和导演关系查询</a>
        </el-menu-item>
        <el-menu-item index="/cooperationSearch">
            <i class="el-icon-search"></i>
            <a slot="title">演员合作关系查询</a>
        </el-menu-item>
        <el-menu-item index="/commentSearch">
            <i class="el-icon-search"></i>
            <a slot="title">按照用户评价查询</a>
        </el-menu-item>
      </el-submenu>

      <el-menu-item index="/comprehensiveSearch">
        <i class="el-icon-search"></i>
        <a slot="title">组合查询</a>
      </el-menu-item>

    </el-menu>
  </el-aside>

</template>

<script>
export default {
  name: 'Sidebar',
  computed:{
  },
  data () {
    return {
      // 初始化选中tab格
      activeIndex: "/"
    }
  },
  methods:{
  }
}
</script>

<!-- 导入sidebar css -->
<style scoped src="../assets/css/sidebar.css"></style>

<style>
    .el-submenu__title {
        color: rgb(191, 203, 217);
    }
</style>