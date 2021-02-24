import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


const store = new Vuex.Store({
    state: {
        sideBarCollapse: false,
    }
})

export default store