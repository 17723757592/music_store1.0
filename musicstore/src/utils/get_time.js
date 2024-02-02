const getTime = function() {
    let dt = new Date()
    var y = dt.getFullYear()
    var mt = (dt.getMonth() + 1).toString().padStart(2,'0')
    var day = dt.getDate().toString().padStart(2,'0')
    var h = dt.getHours().toString().padStart(2,'0')
    var m = dt.getMinutes().toString().padStart(2,'0')
    const nowTime = y + "-" + mt + "-" + day + " " + h + ":" + m 
    return(nowTime)
}
export default getTime