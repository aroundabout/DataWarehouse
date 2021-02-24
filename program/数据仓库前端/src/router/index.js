import Vue from 'vue'
import Router from 'vue-router'

import Home from "@/views/Home";
import TimeSearch from "@/views/TimeSearch";
import MovieName from "@/views/MovieName";
import MovieType from "@/views/MovieType";
import Director from "@/views/Director";
import Actor from "@/views/Actor";
import Relation from "@/views/Relation";
import Comment from "@/views/Comment";
import Cooperation from "@/views/Cooperation";
import Chart from "@/views/Chart";
import ComprehensiveSearch from "@/views/ComprehensiveSearch";


Vue.use(Router)


const routes = [
    {
        path: '/',
        name: 'home',
        component: Home,
        meta: {
            title: '首页',
            name: '首页'
        },

        children: [{
                path: '/timeSearch',
                component: TimeSearch,
                meta: {
                    name: '时间查询'
                }
            },
            {
                path: '/movieNameSearch',
                component: MovieName,
                meta: {
                    name: '电影名称查询'
                }
            },
            {
                path: '/movieTypeSearch',
                component: MovieType,
                meta: {
                    name: '电影种类查询'
                }
            },
            {
                path: '/directorSearch',
                component: Director,
                meta: {
                    name: '电影导演查询'
                }
            },
            {
                path: '/actorSearch',
                component: Actor,
                meta: {
                    name: '电影演员查询'
                }
            },
            {
                path: '/relationSearch',
                component: Relation,
                meta: {
                    name: '演员和导演查询'
                }
            },
            {
                path: '/cooperationSearch',
                component: Cooperation,
                meta: {
                    name: '演员合作查询'
                }
            },
            {
                path: '/commentSearch',
                component: Comment,
                meta: {
                    name: '用户评论查询'
                }
            },
            {
                path: "/chart",
                component: Chart,
                meta: {
                    name: "不同存储模型查询效率比较"
                }
            },
            {
                path: "/comprehensiveSearch",
                component: ComprehensiveSearch,
                meta: {
                    name: "组合查询"
                }
            }
        ]
    }

]

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router