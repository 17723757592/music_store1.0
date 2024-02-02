<template>
    <div class="g-bd">
        <div class="n-rank_web">
            <section class="new-album">
                <h2>新碟上架</h2>
                <ul>
                    <li v-for="(item,index) in productionData.Nalbum" :key="item.data_id" :style="(index+1) % 4 == 0 ? {marginRight:'0px'}:''">
                        <div class="cover-album">
                            <img :src="item.img" alt="">
                        </div>
                        <div class="album-cnt">
                            <h3 class="album-name">{{item.contend}}</h3>
                            <p class="author">{{item.author}}</p>
                            <p class="price">￥{{ item.money }} <span v-show="item.discount" class="tag"><em>{{item.discount}}</em></span>&nbsp;</p>
                        </div>
                    </li>
                </ul>
            </section>
            <div class="sales-rank">
                <div class="board-title">
                    <span class="z-sel">数字专辑榜</span><span class="separate">|</span><span>数据单曲榜</span>
                </div>
                <section class="album-rank">
                    <div class="tab-area">
                        <nav class="u-tab">
                            <a class="tabtitle" href="">
                                <div class="tabtext">
                                    <span class="tt">
                                        <em class="tt-words">日榜</em>
                                        <em class="subtt"></em>
                                    </span>
                                </div>
                            </a>
                            <a class="tabtitle" href="">
                                <div class="tabtext">
                                    <span class="tt">
                                        <em class="tt-words">周榜</em>
                                        <em class="subtt"></em>
                                    </span>
                                </div>
                            </a>
                            <a class="tabtitle" href="">
                                <div class="tabtext">
                                    <span class="tt">
                                        <em class="tt-words">年榜</em>
                                        <em class="subtt"></em>
                                    </span>
                                </div>
                            </a>
                        </nav>
                        <div class="m-tab">
                            <div class="tab-item">
                                <div class="hot-rank">
                                    <ul>
                                        <li class="nav-title">
                                            <span class="index-f1">名次</span>
                                            <span class="index-f2">专辑</span>
                                            <span class="index-f3">销量</span>
                                        </li>
                                        <li v-for="(item,index) in  sortRank" :key="item.data_id">
                                            <span class="album-index">
                                                <em class="num" :style="index > 2 ? {color:'black'} : '#333' ">{{index + 1}}</em>
                                            </span>
                                            <div class="album-msg">
                                                <div class="cover-msg"><img :src="item.img">
                                                </div>
                                                <div class="article">
                                                    <h3 calss="f-thide">{{ item.contend }}</h3>
                                                    <p class="sold"><span class="tit">{{ item.sales }}张</span></p>
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
    name:'AlbumName',
    data(){
        return {
            rankList:[]
        }   
    },
    computed:{
        ...mapState('home',['productionData']),
        // ...mapGetters('home',['rankList']), 浏览器报错 store.home.getters
        sortRank(){
            const arr = this.rankList
            arr.sort((g1,g2) => {
                return g2.sales - g1.sales
            })
            return arr
        }
    },
    mounted(){
        console.log(this.$store.getters);
    },
    watch:{
        productionData:{
            immediate:true,
            deep:true,
            handler(val){
                this.rankList = val.Nalbum
            }
        }
    },
}
</script>

<style lang="less" scoped>
.g-bd{
    padding-bottom: 160px;
    width: 1100px;
    min-height: 750px;
    margin: 0 auto;
    background: #fff;
    .n-rank_web{
        width: 1100px;
        margin: 0 auto;
        .new-album{
            background-color: #fff;
            h2{
                margin: 50px 0 20px 0;
                font-size: 24px;
                text-align: left;
                line-height: 24px;
                font-weight: bold;
            }
            ul{
                overflow: hidden;
                min-height: 664px;
                li{
                    float: left;
                    position: relative;
                    width: 238px;
                    margin-right: 49px;
                    list-style: none;
                    .cover-album{
                        width: 210px;
                        height: 210px;
                        overflow: hidden;
                        padding-top: 0;
                        cursor: pointer;
                        position: relative;
                        background: #e1e3e4;
                        img{
                            display: block;
                            width: 100%;
                            height: 100%;
                        }
                    }
                    .album-cnt{
                        margin-top: 12px;
                        font-size: 14px;
                        padding: 0 33px 50px 0;
                        text-align: center;
                        .album-name{
                            margin-top: 12px;
                            font-weight: bold;
                            font-size: 14px;
                            text-align: center;
                        }
                        .album-name:hover{
                                text-decoration: underline;
                                cursor: pointer;
                            }
                        .author{
                            line-height: 22px;
                            color: #666;
                            word-wrap: normal;
                            overflow: hidden;
                            text-overflow: ellipsis;
                        }
                        .price{
                            font-size: 14px;
                            color: #d33a31;
                        }
                    }
                }
            }
        }
        .sales-rank{
            position: relative;
            .board-title{
                font-weight: bold;
                font-size: 20px;
                color: #999;
                position: absolute;
                top: -56px;
                span{
                    cursor: pointer;
                }
                .z-sel{
                    font-size: 24px;
                    color: #333;
                    font-weight: bold;
                }
                .separate{
                    margin: 0 20px;
                    font-size: 20px;
                    color: rgba(0, 0, 0, 0.1);                 
                }
            }
            .album-rank{
                margin: 120px 0 120px;
                position: relative;
                .tab-area{
                    margin: 0 auto;
                }
                .u-tab{
                    display: block;
                    height: 26px;
                    line-height: 26px;
                    padding: 0;
                    overflow: hidden;
                    position: absolute;
                    top: -48px;
                    width: auto;
                    right: 45px;
                    color: #999;
                    .tabtitle{
                        font-weight: bold;
                        float: left;
                        width: auto;
                        position: relative;
                        margin-right: 40px;
                        ::after{
                            content: '|';
                            position: absolute;
                            left: -23px;
                            color: rgba(0, 0, 0, 0.1);
                        }
                        .tabtext{
                            padding: 0 4px;
                            color: #999;
                            font-size: 14px;
                            line-height: inherit;
                            .tt{
                                display: block;
                                overflow: hidden;
                                text-overflow: ellipsis;
                                white-space: nowrap;
                                .subtt{
                                    margin-left: 5px;
                                    color: #999;
                                    font-size: 13px;
                                    font-style: normal;
                                    vertical-align: baseline;
                                }
                            }
                        }
                        .tabtext:hover span{
                            color: #333;
                        }
                    }
                }
                .m-tab{
                    margin-top: 28px;
                    display: block;
                    width: 100%;
                    height: 100%;
                    .tab-item{
                        width: 100%;
                        height: 100%;
                        .hot-rank{
                            padding-bottom: 10px;
                            border: 1px solid #eee;
                            .nav-title{
                                overflow: hidden;
                                height: 39px;
                                line-height: 39px;
                                padding: 0;
                                margin-bottom: 1px;
                                background: #f4f4f4;
                                color: #999;
                                font-weight: bold;
                                font-size: 14px;
                                span{
                                    float: left;
                                }
                                .index-f1{
                                    width: 90px;
                                    text-align: center;
                                    font-size: 14px;
                                }
                                .index-f2{
                                    width: 420px;
                                    text-align: left;
                                    padding-left: 145px;
                                }
                            }
                            li:hover{
                                background-color: #f4f4f4;
                            }
                            li{
                                padding: 10px 0;
                                .album-index{
                                    color: #d33a31;
                                    font-size: 24px;
                                    float: left;
                                    width: 90px;
                                    margin-top: 28px;
                                    text-align: center;
                                    .num{
                                        font-style: normal;
                                        text-align: left;
                                        font-size: inherit;
                                    }
                                }
                                .album-msg{
                                    overflow: hidden;
                                    height: 100px;
                                    line-height: 100px;
                                    margin-left: 90px;
                                    position: relative;
                                    .cover-msg{
                                        float: left;
                                        width: 100px;
                                        height: 100px;
                                        position: relative;
                                        img{
                                            display: block;
                                            width: 100%;
                                            height: 100%;
                                            position: relative;
                                        }
                                    }
                                    .article{
                                        float: left;
                                        text-align: left;
                                        height: 100%;
                                        margin: 0 10px 0 45px;
                                        font-size: 14px;
                                        h3{
                                            float: left;
                                            width: 370px;
                                            font-weight: normal;
                                            padding-right: 50px;
                                            overflow: hidden;
                                            text-overflow: ellipsis;
                                        }
                                        .sold{
                                            float: left;
                                            font-size: 14px;
                                            color: #999;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
</style>