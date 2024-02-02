
import axios from 'axios'
// import data from '../../../public/data.json'


const state = {
    productionData: JSON.parse(sessionStorage.getItem('productionData')) || [],
    number: JSON.parse(sessionStorage.getItem('number')) || 1   
}

const mutations = {
    JIA(state) {
        state.number = JSON.parse(sessionStorage.getItem('number')) || 1
        state.number++
        // console.log(state);  
    },
    JIAN(state) {
        state.number = JSON.parse(sessionStorage.getItem('number')) || 1
        state.number--

    },
    SET_PRODUCTION_DATA: (state, data) => {
        sessionStorage.setItem('productionData',JSON.stringify(data))
        state.productionData = data
    },
}

const actions = {
    jian(context) {
        if (context.state.number > 1) {
            context.commit('JIAN')
        }
    },
    // console.log(context);
    //actions中拿不到state
    addMessage(context) {
        axios.get('/store_data.json').then(
            response => {
                // console.log(context.state.msg);
                //console.log(response.data);
                context.commit('SET_PRODUCTION_DATA', response.data)
                console.log('获取了axois数据');
                // console.log(context.state.msg);
            },
            error => {
                alert(error.message)
            }
            // function(msg){
            //     console.log(msg.data);
            //}
        )
    },
    // getCategoryList({commit},data){

    //     commit('SET_PRODUCTION_DATA', response.data)
    // }
}
const getters = {
   number(state) {
       return state.number

   },
//    rankList(state) {
//     // production没有即使返回数据sort()会报错
//        return state.productionData.Nalbum.sort((g1,g2) =>{
//            return g2.sales - g1.sales
//         })
//     }
}


export default {
    namespaced: true,//开启名命空间
    state,
    mutations,
    actions,
    getters

    // getters: {
    //     number(state) {
    //         return state.number

    //     },
    // }

}  
