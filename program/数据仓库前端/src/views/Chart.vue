<template>

  <div>

    <el-row>

	<div class="Echarts">
		<div class="charts" id="table" style="width: 1500px;height:600px;"></div>
	</div>

    </el-row>
  </div>
</template>

<script>
export default {
  data(){
    return{
        value: '',
        tableData: []
    }
  },
  created() {
  },
  methods:{
    myEcharts(){
		var myChart=this.$echarts.init(document.getElementById('table'));
		var option = {
			title:{
			text:'查询耗费时间(单位:毫秒ms)',
			textStyle:{
				fontSize:14
			}
			},
			tooltip:{show:true},
			legend:{
				data:['mysql','neo4j','hive']
			},
			xAxis:{
				data:["时间查询","电影名查询","电影种类查询","导演查询","演员查询","用户评分查询","导演和演员关系","演员合作次数"]
			},
			yAxis:{},
			series:[
				{
					name:'mysql',
					type:'bar',
					data:[181.66,180.41,228.21,550.49,298.10,427.04,174.97,184.42],
					label:{
						normal:{
							show:true,
							position:'top'
						}
					}
				},
				{
					name:'neo4j',
					type:'bar',
					data:[182.09,193.43,656.91,326.75,237.80,632.81,220.05,232.61],
					label:{
						normal:{
							show:true,
							position:'top'
						}
					}
				},
				{
					name:'hive',
					type:'bar',
					data:[1670,1590,4570,2100,1680,1830,1770,1610],
					label:{
						normal:{
							show:true,
							position:'top'
						}
					}
				}
				]
			};
		myChart.setOption(option);
		}
	},
  mounted(){
      this.myEcharts();
  }
}
</script>

<style scoped>

.Echarts{
  width:90%;
  display:flex;
  pedding:20px;
}


</style>