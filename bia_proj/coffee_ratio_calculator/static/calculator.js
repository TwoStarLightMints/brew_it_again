import { validate_ratio_input, validate_float_input } from '/static/utils.js';

const calc_button = document.querySelector('#calculate');
const result_paragraph = document.querySelector('p.result');
const result_span = document.querySelector('span.result');
const input_ratio = document.querySelector('#input-ratio')
const input_amount = document.querySelector('#input-amount');
const input_substance = document.querySelector('#w-or-c-label');
const output_substance = document.querySelector('#w-or-c-out');
const substance_in_type_radio = document.querySelectorAll('input[name="w-or-c"]');

Array.from(substance_in_type_radio).forEach(elem => elem.addEventListener('change', e => {
    const substance_in_type_val = document.querySelector('input[name="w-or-c"]:checked').value;

    input_substance.textContent = substance_in_type_val;

    result_paragraph.style.display = 'none';
    result_paragraph.setAttribute('hidden', "");
    result_span.setAttribute('hidden', "");
    output_substance.setAttribute('hidden', "");
}))

function calculate() {
    const [ ratio_num, ratio_den ] = input_ratio.value.split("/").map(n => parseFloat(n));
    const substance_amount = parseFloat(input_amount.value);
    const substance_in_type_val = document.querySelector('input[name="w-or-c"]:checked').value;

    if (substance_in_type_val === "water") {
        result_span.textContent = ((substance_amount * ratio_num) / ratio_den).toFixed(2);
        output_substance.textContent = "coffee";
    } else if (substance_in_type_val === "coffee") {
        result_span.textContent = ((substance_amount * ratio_den) / ratio_num).toFixed(2);
        output_substance.textContent = "water";
    }
    
    result_paragraph.style.display = 'block';
    result_paragraph.removeAttribute('hidden');
    result_span.removeAttribute('hidden');
    output_substance.removeAttribute('hidden');
}

calc_button.addEventListener('click', e => {
    e.preventDefault();
    calculate();
});
