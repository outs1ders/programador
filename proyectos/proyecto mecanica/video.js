var video = document.getElementById("myVideo");
var btn = document.getElementById("myBtn");

function myFunction() {
    if (video.paused) {
    video.play();
    btn.innerHTML = "ver";
    } else {
    video.pause();
    btn.innerHTML = "seguir";
    }
}