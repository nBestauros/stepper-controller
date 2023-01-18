const moveAPI = async (steps, direc) => {
    const APIResponse = await fetch(`/v1/move${direc}?steps=${steps}`)
    console.log(APIResponse)
}

const stopAPI = async () => {
    const APIResponse = await fetch(`/v1/moveStop`)
    console.log(APIResponse)
}

const moveForward = () => {
    let steps = document.getElementById('forwardSteps').value;
    moveAPI(steps, "Forward");
}


const moveBackward = () => {
    let steps = document.getElementById('backwardSteps').value;
    moveAPI(steps, "Backward");
}

const moveStop = () => {
    stopAPI();
}

document.getElementById("forwardButton").addEventListener("click", moveForward)
document.getElementById("backwardButton").addEventListener("click", moveBackward)
document.getElementById("stopButton").addEventListener("click", moveStop)