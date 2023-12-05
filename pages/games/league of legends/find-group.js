let gamemodes = ["Ranked Solo/Duo", "Ranked Flex", "Normal", "ARAM", "Frenesi"]
let servers = ["NA", "KR", "LAS", "LAN", "EUW"]

// seleccionar un modo de juego random
function selectGamemode() {
    let randomGamemode = Math.floor(Math.random() * gamemodes.length); 
    return gamemodes[randomGamemode];
}
// llevar el modo de juego random al HTML
function uploadGamemode(){
    for (let i = 1; i <= gamemodes.length; i++) {
        let span = document.getElementById(`Gamemode${i}`);
        span.textContent = selectGamemode();
    }
}

// seleccionar un servidor random
function selectServer() {
    let randomServer = Math.floor(Math.random() * servers.length);
    return servers[randomServer];
}
// llevar el servidor random al HTML
function uploadServer() {
    for (let i = 0; i <= servers.length; i++){
        let span = document.getElementById(`Server${i + 1}`);
        span.textContent = selectServer();
    }
}

uploadGamemode();
uploadServer();

function getRandomNames() {
    return fetch('https://randomuser.me/api')
        .then(response => response.json())
        .then(randomname => randomname.results[0].name.first)
}


const names = document.querySelectorAll("li")

names.forEach(async function(name) {
    let randomName = await getRandomNames();
    name.textContent = randomName;
});
