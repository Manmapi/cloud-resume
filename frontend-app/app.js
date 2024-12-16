const base_url = "https://omrag3vlab.execute-api.ap-southeast-1.amazonaws.com/prod/counter?name=visited"

const getVisitedCount = () => {
    const options = {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        }
    }
    fetch(base_url, options).then(response => response.json())
    .then(data => {
        let count = data["counted"]["N"]
        const counterDisplay = document.querySelector(".counter-display")
        counterDisplay.textContent=count
    }).catch(console.error)
}
const updateVisitedCount = () => {
    const options = {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        }
    }
    fetch(base_url, options).catch(console.error)
}

if(window.attachEvent) {
    window.attachEvent('onload', yourFunctionName);
} else {
    if(window.onload) {
        var curronload = window.onload;
        var newonload = function(evt) {
            curronload(evt);
            updateVisitedCount(evt);
            getVisitedCount(evt);
        };
        window.onload = newonload;
    } else {
        window.onload = function(evt) {
            updateVisitedCount(evt);
            getVisitedCount(evt);
        };
    }
}