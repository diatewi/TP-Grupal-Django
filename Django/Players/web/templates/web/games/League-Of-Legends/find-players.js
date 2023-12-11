let servers = ["NA", "KR", "LAS", "LAN", "EUW"]

function selectServer() {
    let randomServer = Math.floor(Math.random() * servers.length);
    return servers[randomServer];
}
// llevar el servidor random al HTML
function uploadServer() {
    let articles = document.querySelectorAll('article.groups.players')
    articles.forEach((article) => {
        let span = article.querySelector('span');
        span.textContent = selectServer();
    });
}

uploadServer()

function getRandomNames() {
    return fetch('https://randomuser.me/api')
        .then(response => response.json())
        .then(randomname => randomname.results[0].name.first)
}
document.addEventListener("DOMContentLoaded", async function () {
    const names = document.getElementsByClassName("user");

    for (const name of names) {
        let randomName = await getRandomNames();
        name.textContent = randomName;
    }
});