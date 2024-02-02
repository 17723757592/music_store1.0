<template>
    <!-- 底部版权相关信息 -->
    <div class="bottom">
        <div class="bottom-m">
            <div class="copy">
                <p class="bottomcopy3">
                    <span>版权所有©2023</span>
                    备案号:
                    <a href="https://beian.miit.gov.cn/#/Integrated/index"
                        >渝xxxxxxxxxxx</a
                    >
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "BottomName",
};
</script>

<style>
.bottom {
    /* width: 1100px; */
    /* margin: 0 auto; */
    background: #f2f2f2;
}
.copy {
    font-size: 12px;
    padding: 10px 0px;
    line-height: 24px;
}
.copy p a:hover {
    text-decoration: underline;
}
.copyline {
    margin: 0 8px 0 10px;
    color: #c2c2c2;
    line-height: 24px;
}
.bottomcopy a {
    color: #999;
}
.bottomcopy3 span {
    margin-right: 14px;
}
</style>
