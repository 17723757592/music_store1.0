
export default {
    namespaced: true,
    state: {
        shoppingCart:JSON.parse(sessionStorage.getItem('shoppingCart')) || [],
    },
    mutations: {
            // let a = [1,2,3,4]    

            // a.forEach()
            // a.map((row) => {
            //     // do something
            //     return ''
            // })
            // a.filter((row) => {
            //     return true || false
            // })
            // a.find()

            // a.every()
            // a.some((row) => {
            //     return true || false
            // })

            // a.reduce((prevData, row) => {

            //     if (xxx) {
            //         return prevData + 5
            //     }
            // }, 0)

            // 栈结构
            // 双向链表
            // 单项链表


            // a.unshift()
            // a.shift()
            // a.pop()
            // a.push()

            // a.slice()
            // a.join()

            // Array.isArray(a)

            // a.includes()
            // a.indexOf()

            // a.at(-1)
            // a[a.length - 1]

            // a.length = 0
            // a
        JIA(state, id) {
            state.shoppingCart.forEach((item) => {
                if (item.id === id) { item.number++ }
            })
            // console.log(state);  
        },
        JIAN(state, id) {
            state.shoppingCart.forEach((item) => {
                if (item.id === id) {
                    item.number--
                }
            })
        },
        changeNumber(state, {id, put}){
            state.shoppingCart.forEach((item) => {
                    if (item.id === id){
                        item.number = put
                    }
                })
        },
        resetShoppingCart(state) {
            // 设置购物车状态
            state.shoppingCart = state.shoppingCart.filter((item) =>{
                return item.check == false
            });
            sessionStorage.setItem('shoppingCart', JSON.stringify(state.shoppingCart))
        },
        unshiftShoppingCart(state, data) {
            // 添加购物车
            // 用于在商品详情页点击添加购物车,后台添加成功后，更新vuex状态
            state.shoppingCart.unshift(data)
            sessionStorage.setItem('shoppingCart', JSON.stringify(state.shoppingCart))
        },
        deleteShoppingCart(state, id) {
            if (confirm('确定删除吗？')) {
                state.shoppingCart = state.shoppingCart.filter((item) => {
                    return item.id != id
                })
                sessionStorage.setItem('shoppingCart', JSON.stringify(state.shoppingCart))
            }
        },
        changeCheck(state, id) {
            state.shoppingCart.forEach((item) => {
                if (item.id === id) { item.check = !item.check }
            })
        },
        changeAllCheck(state, data){
            state.shoppingCart.forEach((item) => {
                    item.check = data
            })
        },

    },
    actions: {
        // getShoppingCartNumber(context,id){
        //     const Item = context.state.shoppingCart.find((item) => item.id === id)
        //     console.log(Item.number)
        //     return Item.number
        // },
        jian(context, id) {
            context.state.shoppingCart.forEach((item) => {
                if (item.id === id && item.number > 1) {
                    context.commit('JIAN', id)
                }
            })
        },
        changeNumber(context, {id, put}){
            if(put){
                context.commit('changeNumber',{id,put})
            }
        },
        unshiftShoppingCart({ commit }, data) {
            commit('unshiftShoppingCart', data);
        },
        changeAllCheck(context,data){
            if (context.state.shoppingCart.length > 0){
                context.commit('changeAllCheck',data)
            }
        }

    },
    getters: {
        getShoppingCartNumber:(state) =>  {
            return(id) => state.shoppingCart.find(item=>item.id == id)
          },

        getTotalPrice(state) {
            // 购物车勾选的商品总价格
            let totalPrice = 0;
            for (let i = 0; i < state.shoppingCart.length; i++) {
                const temp = state.shoppingCart[i];
                if (temp.check) {
                    totalPrice += temp.price * temp.number;
                }
            }
            return totalPrice;
        },
        checkedNumber(state){
            let checkedNumber = 0
            for (let i = 0; i < state.shoppingCart.length; i++){
                const temp = state.shoppingCart[i];
                if(temp.check){
                    checkedNumber += 1
                }
            }
            return checkedNumber
        },
        checkedShoppingCart(state){
            const checkedShoppingCart = state.shoppingCart.filter((item) => item.check == true)
            return checkedShoppingCart
        } ,
        // payed:(state)=>{
        //    return(data) =>{
        //     state.getPay => {state.getPay = data}
        //    }
        // }
    },
}