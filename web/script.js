function main() {
    const playBtn = document.querySelector("#play_btn")
    playBtn.addEventListener(('click'), () => call_in_python())
    // const openBtn = document.querySelector("#open")
    // playBtn.addEventListener(('click'), () => select())
}

main()

async function call_in_python() {
    const speed = document.getElementById('speed').value;
    const progress = document.getElementById('progress').value;
    const word = await eel.set_values(speed, progress)();
    document.getElementById('word').innerHTML = word;
    // console.log(word)
}

eel.expose(showWords);
function showWords(word){
    document.getElementById('word').value = word;
    // console.log(word);
}

eel.expose(showProgress);
function showProgress(progress){
    document.getElementById('progress').value = progress;
    document.getElementById('progress_bar').value = progress;
    // console.log(word);
}


// async function select(){
//     eel.selectFolder();
// }