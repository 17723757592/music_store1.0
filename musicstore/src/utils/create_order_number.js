const createOrderNumber = function(){
    let now = new Date();
    let year = now.getFullYear();       //年
    let month = now.getMonth() + 1;     //月
    let day = now.getDate();            //日
    let hh = now.getHours();            //时
    let mm = now.getMinutes();          //分
    let ss = now.getSeconds();           //秒
    let clock_number = year + "";
    if(month < 10){
        clock_number += "0";
    }
    clock_number += month + "";
    if(day < 10){
        clock_number += "0";
    }
    clock_number += day + "";
    if(hh < 10){
        clock_number += "0";
    }
    clock_number += hh + "";
    if(mm < 10){
        clock_number += '0';
    } 
    clock_number += mm + "";
    if(ss < 10){
        clock_number += '0';
    } 
    clock_number += ss;
    return(clock_number);
}
export default createOrderNumber