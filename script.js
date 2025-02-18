function collectResource(resource) {
    fetch(`/collect/${resource}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById("resource-count").innerText = 
            `Resources: ${data.Wood} Wood, ${data.Apple} Apple`;
    });
}
