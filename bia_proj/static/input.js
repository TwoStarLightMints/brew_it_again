import { validate_integer_input, validate_float_input, validate_ratio_input, validate_brew_time_input } from '/static/utils.js';

Array.from(document.querySelectorAll('.integer-input')).forEach(elem => elem.addEventListener('keyup', e => { validate_integer_input(e) }));
Array.from(document.querySelectorAll('.float-input')).forEach(elem => elem.addEventListener('keyup', e => { validate_float_input(e) }));
Array.from(document.querySelectorAll('.ratio-input')).forEach(elem => elem.addEventListener('keyup', e => { validate_ratio_input(e) }));
Array.from(document.querySelectorAll('.brew-time-input')).forEach(elem => elem.addEventListener('keyup', e => { validate_brew_time_input(e) }));
