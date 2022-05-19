const canvasIn = document.getElementById("canvas-in");
const ctx = canvasIn.getContext("2d");
const reader = new FileReader();
const img = new Image();

const canvasOut = document.getElementById("canvas-out");
const ctxOut = canvasOut.getContext("2d");
const imgOutput = new Image();

function performAdptThr() {
    // HTTP POST Request using fetch API / axios

    if (img) {
        axios.post('http://127.0.0.1:5000/adaptive', {
                imageData: img.src,
            })
            .then(function (response) {

                data = response.data['outputImage'];
                // Callback function to display resultant image onto canvas-out
                console.log(data)
                displayResultant(data);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

}

function displayResultant(imgString) {
    imgOutput.src = imgString;
    imgOutput.onload = () => {
        canvasOut.width = img.width;
        canvasOut.height = img.height;
        ctxOut.drawImage(imgOutput, 0, 0);
    }
}

const uploadImage = (e) => {
    reader.onload = () => {
        img.onload = () => {
            canvasIn.width = img.width;
            canvasIn.height = img.height;
            ctx.drawImage(img, 0, 0);
        };
        img.src = reader.result;
    };
    reader.readAsDataURL(e.target.files[0]);
};
const imageLoader = document.getElementById("imgUpload");
imageLoader.addEventListener("change", uploadImage);

function download() {
    const image = canvasIn.toDataURL();
    const link = document.createElement("a");
    link.href = image;
    link.download = "image.png";
    link.click();
}
document.querySelector("#download").addEventListener("click", download);