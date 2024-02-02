import VueRouter from 'vue-router'
import SortPage from '../views/Sort.vue'
import HomePage from '../components/home/HomePage.vue'
import DetailName from '../details/Detail.vue'
import BusName from '../store_bus/Bus.vue'
import BeSure from '../store_bus/BeSure.vue'
import PersonalCenter from '../user/user.vue'
import PerOrder from '../user/PerOrder.vue'
import PerDiscount from '../user/PerDiscount.vue'
import PerAddress from '../user/PerAddress.vue'
import CustomerSevice from '../user/CustomerSevice.vue'
import EarphoneName from '../components/page/earphone.vue'
import HotPeripheral from '../components/page/HotPeripheral.vue'
import AlbumName from '../album/album.vue'

const router =  new VueRouter({
    routes:[
        {
           path:'/',
           name:'home',
           component:HomePage,
        },
        {
            path:'/earphone',
            name:'earphone',
            component:EarphoneName
        },
        {
            path:"/hotperipheral",
            name:"hotperipheral",
            component:HotPeripheral
        },
        {
            path:'/album',
            name:'album',
            component:AlbumName
        },
        {
            path:'/sort/:bread',
            name:'sort',
            component:SortPage,
            props($router) {
                return {
                  bread: $router.params.bread,
                }
            }
        },
        {
            path:'/detail/:bread?/:title/:id',
            name:'detail',
            meta:{title:'商品详情'},
            component:DetailName,
            props($router) {
                return {    
                    bread:$router.params.bread,
                    titleR: $router.params.title,
                    id:$router.params.id
                }
            }
        },
        {
            path:'/bus',
            name:'bus',
            meta:{title:'购物车'},
            component:BusName,

        },
        {
            path:'/order',
            name:'order',
            meta:{isAuth:true,title:'确认订单'},
            component:BeSure,
        },
        {
            path:'/personalcenter/:bread',
            name:'personalcenter',
            meta:{title:'个人中心'},
            redirect:'/personalcenter/:bread/perorder',
            component:PersonalCenter,
            props($router) {
                return {
                  bread: $router.params.bread,
                }
            },
            children:[
                {
                    name:'perorder',
                    path:'perorder',
                    component:PerOrder,
                    // props($router) {
                    //     return {
                    //       confirmAddress:$router.params.confirmAddress
                    //     }
                    // }
                },
                {
                    name:'perdiscount',
                    path:'perdiscount',
                    component:PerDiscount
                },
                {
                    name:'peraddress',
                    path:'peraddress',
                    component:PerAddress
                },
                {
                    name:'customersevice',
                    path:'customersevice',
                    component:CustomerSevice
                }
            ]
        }
    ],
})
router.afterEach((to) => {
    window.scrollTo(0,0);
    if(to.meta.title){ 
        document.title = to.meta.title //修改网页的title
    }else{
        document.title = 'musicstore'
    }
})
export default router