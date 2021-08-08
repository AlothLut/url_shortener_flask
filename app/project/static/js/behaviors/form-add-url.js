import {AddUrl} from "../components/AddUrl.js"

document.addEventListener("DOMContentLoaded", function () {
    const addUrlForm = document.querySelector(".js-add-url");

    if (addUrlForm) {
        new AddUrl(addUrlForm)
    }
});