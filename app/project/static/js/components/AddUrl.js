export class AddUrl {
    constructor(node) {
        this.node = node;
        this.result = node.querySelector(".result");
        this.form = node.querySelector("form");
        this.action = this.form.getAttribute("action");

        this.setListeners();
    }

    setListeners() {
        this.form.addEventListener("submit", (e) => {
            e.preventDefault();
            this.handleFormSubmit();
        })
    }


    async handleFormSubmit() {
        let data = new FormData(this.form);
        data = await this.setRecaptchaToken(data);
        try {
            const response = await fetch(this.action, {
                method: "POST",
                body: data,
            });
            const result = await response.json();

            this.showResult(result.message, result.alias);
        } catch (e) {
            console.log(e);
        }
    }

    async setRecaptchaToken(data) {
        let site_key = this.node.getAttribute("data-recaptcha-site-key")
        if (site_key == "") {
            return data;
        }
        const token = await new Promise((resolve) => {
            grecaptcha.ready(async () => {
                resolve(await grecaptcha.execute(site_key, {
                    action: "addShortUrl"
                }));
            });
        });
        data.append("recaptchaToken", token);
        return data;
    }

    showResult(result, alias="") {
        this.result.innerHTML = result + "   " + alias;
    }
}