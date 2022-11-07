function main() {
    const playBtn = document.querySelector("#play_btn")
    playBtn.addEventListener(('click'), () => call_in_python())
}

main()

async function call_in_python() {
    const speed = document.getElementById('speed').value;
    const progress = document.getElementById('progress').value;
    const word = await eel.set_values(speed, progress)();
    document.getElementById('word').innerHTML = word;
    // console.log(word)
}


eel.expose(showJs);
function showJs(word){
    document.getElementById('word').value = word;
    // console.log(word);
}
