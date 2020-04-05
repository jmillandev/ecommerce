const $form = document.getElementById('promocode-form')

$form.addEventListener('submit', function(event) {
    event.preventDefault()

    const code = this.code.value
    const url = `${this.action}?code=${code}`

    fetch(url)
        .then(response => response.json())
        .then( response => {
            const $discount = document.getElementById('discount')
            const $total = document.getElementById('total_price')
            const $message = document.getElementById('promocode_message')
            if (response.status === true) {
                $message.classList.remove('text-danger')
                $message.classList.add('text-success')
                $message.innerText = response.message

                $discount.innerText = `$${response.discount}`
                $total.innerText = `$${response.total}`
                this.code.disabled = True
            } else {
                $message.classList.add('text-danger')
                $message.classList.remove('text-success')
                $message.innerText = response.message
            }
            console.log(response)
        })

})