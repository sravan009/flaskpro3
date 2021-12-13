async function calculate(form){
    event.preventDefault();
    const opt = {
        method: 'POST',
        headers: { 'content-Type': 'application/json' },
        body: JSON.stringify({
            number1: parseInt(form.number1.value),
            number2: parseInt(form.number1.value),
            type: form.type.value
        })
    }
    const req = await fetch("/calculate", options);
    const resp = await req.json();
    if (resp.success){
        const answerDiv = document.querySelector("result");
        answerDiv.style.color = "blue";
        answerDiv.innerText = resp.result;

    } else {
        const answerDiv = document.querySelector(".result")
        answerDiv.style.color = "blue";
        answerDiv.innerText = resp.error;
    }

}