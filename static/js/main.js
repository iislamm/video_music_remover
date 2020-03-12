// const url = 'http://vmr-main.g2u3wc8vm9.us-east-2.elasticbeanstalk.com/video';
const url = '/video';

document.getElementById("video-form").onsubmit = handleSubmit

function handleSubmit(e) {
    e.preventDefault();
    var form_data = new FormData($('#video-form')[0]);
    $("#loading-container").append("Loading...")
    $.ajax({
        type: 'POST',
        url,
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
    success:function(res){
        console.log(res)
        $("#loading-container").append("Done")
        $("#output-video").attr("src", res.video_path.substr(1))
        $("#output").show()
   },
   error:function(data){
            console.log("error");
            console.log(data);
            $("#loading-container").append("An Error occured")
        }
    });
  };