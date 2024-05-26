const unit_selector = document.querySelector("#unit");
const water_radio = document.querySelector("#water-radio");
const coffee_radio = document.querySelector("#coffee-radio");
const calc_display = document.querySelector('#display');
const clear_button = document.querySelector('#clear');
const del_button = document.querySelector('#delete');
const calc_button = document.querySelector('#calculate');
const num_buttons = document.querySelectorAll('.number');

// True == water | False == coffee
let curr_unit = true;

function load_unit_opts() {
    function clear_unit_opts() {
        Array.from(unit_selector.children).forEach(e => unit_selector.remove(e));
    }

    if (curr_unit) {
        clear_unit_opts();

        water_units.forEach(e => {
            unit_selector.appendChild(e);
        });

        unit_selector.value = water_units[0].value;
    } else {
        clear_unit_opts();

        coffee_units.forEach(e => {
            unit_selector.appendChild(e);
        });

        unit_selector.value = coffee_units[0].value;
    }

    curr_unit = !curr_unit;
}

// The units which will appear in the drop down will be stored and managed here
const coffee_units = [
    Object.assign(document.createElement('option'), {value: 'ounces', textContent: 'Ounces'}),
    Object.assign(document.createElement('option'), {value: 'grams', textContent: 'Grams'}),
];

const water_units = [
    Object.assign(document.createElement('option'), {value: 'fluid-ounces', textContent: 'Fluid Ounces'}),
    Object.assign(document.createElement('option'), {value: 'milliliters', textContent: 'Milliliters'}),
];

water_radio.addEventListener("change", ev => { load_unit_opts(); } );
coffee_radio.addEventListener("change", ev => { load_unit_opts(); } );

// Load initial unit options
load_unit_opts();

Array.from(num_buttons).forEach(e => {
    e.addEventListener("click", ev => {
        const curr_content = calc_display.textContent;
        const this_button = ev.target;

        if (curr_content.length == 1 && curr_content[0] == "0" && this_button != ".")
            calc_display.textContent = this_button.textContent;
        else if (this_button == "." && !curr_content.includes("."))
            ;
    });
});

function clear_calculator() {
    calc_display.textContent = '0';
}

function delete_calculator() {

}

function calculate() {

}

clear_button.addEventListener('click', e => {
    clear_calculator();
});

del_button.addEventListener('click', e => {
    delete_calculator();
});

calc_button.addEventListener('click', e => {
    calculate();
});