import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';
import router from './router'
import store from './store'
import axios from 'axios'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import echarts from 'echarts'

import './assets/css/global.css'


Vue.prototype.$axios = axios
Vue.prototype.$echarts = echarts
Vue.use(ElementUI);
Vue.use(mavonEditor)
Vue.config.productionTip = false



router.beforeEach((to, from, next) => {
    /* 路由发生变化修改页面title */
    // if (to.meta.title) {
    //   document.title = to.meta.title
    // }
    // next()

    //必须登录才能访问其他界面
    /*     if (to.path === '/login' || to.path === '/register') return next();
        const login = sessionStorage.getItem("userid");
        if (!login) return next('/login'); */
    next();
})

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
});