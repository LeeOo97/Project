function check_filter(){
    if (document.getElementById("filters").checked==true){
        document.getElementById("filter_k").classList.remove("d-none")
        document.getElementById("filter_max").classList.remove("d-none")
    } else {
        document.getElementById("filter_k").classList.add("d-none")
        document.getElementById("filter_max").classList.add("d-none")
    }
}