<template>
    <!-- Ip周边 -->
    <div>
        <div class="g-bg g-footer">
            <SortTop :bread="bread"></SortTop>
            <div class="g-main">
                <div><FiltersName :bread="bread"></FiltersName></div>
                <div><ModulesName :bread="bread"></ModulesName></div>
            </div>
        </div>
    </div>
</template>

<script>
import SortTop from "./SortTop.vue";
import FiltersName from "./Filters.vue";
import ModulesName from "./Modules.vue";

export default {
    name: "SortPage",
    props: ["bread"],
    components: { SortTop, FiltersName, ModulesName },
};
</script>

<style>
.active {
    font-weight: bold;
    color: #333;
}
.g-bg {
    width: 1100px;
    min-height: 750px;
    margin: 0 auto;
    background: #fff;
}
.g-footer {
    /* padding-bottom: 160px; */
    min-height: calc(100% - 73px - 160px);
}
</style>
