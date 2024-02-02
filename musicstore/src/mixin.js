
import axios from "axios"
export default{
    name:'mixin',
    data() {
        return {
            goodsData:'',
            statu:false
        }
    },
    methods: {
        addItem(){
            axios.get('/store_item.json').then(
                response => {
                    this.goodsData = response.data.goods
                    console.log(this.goodsData);
                },
                error => {
                    alert(error.message)
                }
            )
        },

        /**
         *  
         * @param {Number|String} id 
         * @param {Array} goodsData 
         * @returns {Object}
         */
        queryDataId(id,goodsData){
            return goodsData.filter(row => id === row.id)

            // for (var i = 0; i < goodsData.length; i++) {
            //     if (id==goodsData[i].id){
            //         this.statu = true
            //        return goodsData[i]
            //     }
            // }
        },
        clearData(){
            
        }
    },

}