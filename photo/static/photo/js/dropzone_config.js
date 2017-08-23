// "myAwesomeDropzone" is the camelized version of the HTML element's ID
Dropzone.options.myAwesomeDropzone = {
	paramName: function(){
		return "files";
	}, // The name that will be used to transfer the file
	//paramName: "files",
	addRemoveLinks: true,
	maxFilesize: 10, // MB
	acceptedFiles: ".png,.jpg,.gif,.bmp,.jpeg",
	parallelUploads: 10,
	uploadMultiple: true,
	autoProcessQueue: false,
	dictCancelUpload: "Cancel",
	init:function(){
		$(".dropzone-submit").click(function(){
			var myDropzone = Dropzone.forElement(".dropzone");
			myDropzone.processQueue();
		});
		this.on('complete', function(){
			this.removeAllFiles();			
		});
	},
	/*
	accept: function(file, done) {
		if (file.name == "justinbieber.jpg") {
		  done("you can't upload this file")
		}
		else { done(); }
	}
	*/
};

/*
$("document").ready(function(){
	$(".dropzone-submit").click(function(){
		var dropzone = $(".dropzone");
		alert(dropzone.length);
		dropzone.processQueue();
	});
	
});
*/

