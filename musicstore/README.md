# musicstore

## Project setup
```
npm install
```
css
脱离文档流的特点：
元素不再单独占一行，块元素的默认宽度和高度是被内容撑开的范围。  
相对定位：
若不设置偏移量，元素不发生任何变化，提升元素层次（覆盖其他的元素）但不改变元素性质（块？ 行内？）
相对定位参考的是元素在文档流的原始位置进行定位，而浮动是参考其父元素
绝对定位：
元素提升层次且脱离文档流
相对于其包含块进行定位，行内->块  块内高度默认被内容撑开

margin:  padding:  min-height
外边距，  内边距    设置盒子的最小高度

visibility
隐藏元素后，继续占有原来位置。
如果隐藏元素想要原来位置，就用visibility：hidden
如果隐藏元素不想要原来位置，就用display：none

clear:both
清楚所有浮动

hover
xxx:hover > xxx1      控制xxx元素的子元素
xxx:hover xxx1        控制xxx元素的后代元素
xxx:hover + xxx1      ‘+’ 控制同级元素（兄弟元素）
选择的是item-son紧跟着后面的span元素，是递进的关系,是该兄弟元素与其相邻
xxx:hover ~xxx1       控制兄弟元素，可以不相邻

border-bottom: 1px solid rgba(0, 0, 0, 0.1);
设定元素的边框为1像素宽，实线 颜色？->rgba

display 
(1)其中块级元素对应display：block   <h1>~<h6>,<p>,<div>,<ul>,<ol>,<li>
(2)行内元素对应display：inline。    <a>,<strong>,<b>,<em>,<del>,<span>         
                                                                        和相邻的行内元素在一行上高度和宽度无效，但是水平方向上的padding和margin可以设置，垂直方向上的无效
                                                                        默认的宽度就是它本身的宽度
                                                                        行内元素只能容纳纯文本或者是其他的行内元素（a标签除外

(3)可以通过修改元素的display属性来切换行内元素和块级元素。
(4)display：inline-block；可以让元素具有块级元素和行内元素的特性：既可以设置长宽，可以让padding和margin生效，又可以和其他行内元素并排
                                   img, input, textarea，span

cursor : 
网页浏览时用户鼠标指针的样式或图形形状。
属性值：
default：默认光标（通常是一个箭头）
auto：默认，浏览器设置的光标
crosshair：光标为十字线
pointer：光标为一只手
move：光标为某对象可移动
text：光标指示文本
wait：光标指示程序正在忙（通常是一只表或者一个沙漏）

导入图片：
 data(){
        return {
            n:0,
            img:require('../assets/dot_hover.png'),
            interId:null
        }
 }
 给父元素添加
 overflow:hidden
 清除浮动

window.pageYOffset 
返回文档当前沿垂直轴（即向上或向下）滚动的像素数，其值为0.0，表示该Document的顶部边缘当前与窗口内容区域的顶部边缘对齐。 pageYOffset是scrollY的一个别名是 window的只读属性

document.body.scrollTop;
网页被卷去的高

全局事件总线
this.$bus.$on， 一定要保证先于this.$bus.$emit先执行， 否则接收数据的组件是接收不到数据的。
mutation,action 默认两个参数，第一个参数是， state/context，如果希望传入多个数据可以加一个{data1, data2} 将他们包起来

行内文本超出，省略号显示
white-space:nowrap; 
overflow: hidden;
text-overflow: ellipsis;

期望同一个路由参数不同时也要刷新页面：
router-view就是要添加路由页面的地方，加个key,当key不同时，就会刷新。此时为了保证同一个路由，参数不同时也要刷新，可以将$router.fullPath设置为key。
<router-view :key="$route.fullPath"></router-view>

$route, $router
$route对象表示当前的路由信息，包含了当前 URL 解析得到的信息。包含当前的路径，参数，query对象等。可以找到$route.path/hash/fullPath等
$router为VueRouter实例，想要导航到不同URL，则使用router.push方法


### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

promise不传入resolve的时候（没有调用resolve（））.then（）方法会被挂起，不会被执行
const p1 = () => (new Promise((resolve, reject) => {
 console.log(1);
 let p2 = new Promise((resolve, reject) => {
  console.log(2);
  const timeOut1 = setTimeout(() => {
   console.log(3);
   resolve(4);
  }, 0)
  resolve(5);
 });
 resolve(6);
 p2.then((arg) => {
  console.log(arg);
 });
 
}));
const timeOut2 = setTimeout(() => {
 console.log(8);
 const p3 = new Promise(reject => {
  reject(9);
 }).then(res => {
  console.log(res)
 })
}, 1000)
 

p1().then((arg) => {
 console.log(arg);
});
console.log(10);

（同步任务入栈）普通函数(p1,p2) -> (异步任务入列)(.then()方法，看谁先resolve()) ->(异步任务入列)宏任务(timeout()  看入列时间，看延迟时间决定先后)

1 2 10 5 6 3 8 9


同步代码
所有微任务
第一个宏任务
（如果有第二级且是微任务可以插队，否则先不执行）
同级下一个宏任务
（如果有第二级且是微任务可以插队，否则先执行上一宏任务的二级宏任务）