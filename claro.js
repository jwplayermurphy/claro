jwplayer("jwp").on("error",function(e){
	 var element = document.getElementsByClassName("jw-error-text jw-reset-text")
	 // 232403 error code relates to geoblocking being active
	 if (e.code === 232403 || e.code === 224003) {
	     element[0].innerHTML = "Este video no esta autorizado en su ubicacion";
			}
});
