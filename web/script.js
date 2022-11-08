let flagPlay = 0

function main() {
    const playBtn = document.querySelector("#play_btn")
    playBtn.addEventListener(('click'), () => {
        setFlag();
        if (flagPlay == 0) {
            call_in_python();
            console.log('main 1', flagPlay);
        } else {
            playReading();
            console.log('main 2', flagPlay);
        }
        console.log('main 3', flagPlay);
    })
}

main()

async function call_in_python() {
    const speed = document.getElementById('speed').value;
    const progress = document.getElementById('progress').value;
    const word = await eel.set_values(speed, progress)();
    // console.log(word)
}

eel.expose(showWords);
function showWords(word){
    playReading()
    document.getElementById('word').value = word;
    // console.log(word);
}

eel.expose(showProgress);
function showProgress(progress){
    document.getElementById('progress').value = progress;
    document.getElementById('progress_bar').value = progress;
    // console.log(word);
}

function setFlag(){
    if (flagPlay == 1){
        flagPlay = 0
    } else {
        flagPlay = 1
    }
    console.log('setFlag', flagPlay)
}

eel.expose(playReading);
async function playReading(){
    eel.play_reading(flagPlay)();
    console.log('playReading', flagPlay)
}

// async function select(){
//     eel.selectFolder();
// }